import os
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests.kbase_ui.expected_conditions import (element_attribute_has_value,
                                                element_attribute_is_value)

DEFAULT_TIMEOUT = 10  # seconds

class TestBase(unittest.TestCase):
    def __init__(self, *args):
        self.kbase_host = self.kbase_host_from_env()
        self.run_headless = self.get_headless_from_env()
        self.run_insecure = os.environ.get("INSECURE") == "t"
        self.run_browser = os.environ.get("BROWSER") or "chrome"
        if self.run_browser not in ["chrome", "firefox"]:
            raise ValueError(
                (
                    'The "BROWSER" environment variable may only be set to "chrome" or "firefox";'
                    f' "{self.run_browser}" is not a supported browser; it defaults to "chrome"'
                )
            )
        self.timeout = self.get_timeout_from_env()
        super().__init__(*args)

    def get_headless_from_env(self):
        headless_env = os.environ.get("HEADLESS") or "t"
        if headless_env == "t":
            return True
        if headless_env == "f":
            return False
        raise ValueError(
            (
                'The "HEADLESS" environment variable must be "t", "f" or omitted; '
                f'it was set to "{headless_env}"; '
                'it defaults to "t"'
            )
        )

    def get_timeout_from_env(self):
        timeout_env = os.environ.get("TIMEOUT")
        if timeout_env is None:
            return DEFAULT_TIMEOUT
        try:
            return float(timeout_env)
        except ValueError as ve:
            raise ValueError(
                (
                    'The "TIMEOUT" environment variable must be a number number; '
                    f'"{timeout_env}" is no good; it defaults to "30"'
                )
            )

    def kbase_host_from_env(self):
        env = os.environ.get("KBASE_ENV")
        if env is None:
            return "ci.kbase.us"
        if env in ["ci", "next", "narrative-dev", "appdev"]:
            return f"{env}.kbase.us"
        if env == "prod":
            return "kbase.us"
        raise ValueError(
            (
                'The "KBASE_ENV" environment variable is incorrect; '
                f'"{env}" is not a recognized KBase deployment environment; '
                'supported environments are "ci", "next", "appdev", "narrative-dev" and "prod"; '
                'it defaults to "ci"'
            )
        )

    def setup_chrome(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        if self.run_headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")

        # If a CORS error is thrown for external apis (e.g. genome publications), enabling
        # these lines may reveal an underlying error (as many sites don't have cors set up
        # correctly for error responses.)
        # chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--disable-site-isolation-trials")

        if self.run_insecure:
            chrome_options.add_argument("--ignore-certificate-errors")

        self.browser = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager().install()), options=chrome_options
        )
        self.wait = WebDriverWait(self.browser, self.timeout)

    def setup_firefox(self):
        firefox_options = FirefoxOptions()

        if self.run_headless:
            firefox_options.add_argument("--headless")
        if self.run_insecure:
            firefox_options.accept_insecure_certs = True

        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        self.browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options,
        )
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.actions = ActionChains(self.browser)

    def setUp(self):
        if self.run_browser == "chrome":
            self.setup_chrome()
        elif self.run_browser == "firefox":
            self.setup_firefox()
        self.browser.implicitly_wait(DEFAULT_TIMEOUT)

    def login(self):
        self.browser.delete_all_cookies()
        self.browser.add_cookie(
            {
                "name": "kbase_session",
                "path": "/",
                "value": os.environ.get("KBASE_TOKEN"),
            }
        )

        # self.wait_for_presence("label", "username")

        # self.wait_for_presence("image", "avatar")
        self.wait_for_presence_xpath('//*[@role="button" and @id="user-button"]')

    def logout(self):
        self.browser.delete_all_cookies()

    def navigate(self, path):
        self.browser.get(f"https://{self.kbase_host}/#{path}")

    def login_navigate(self, path):
        """
        Navigate to the given path after "login"
        """
        self.browser.get(f"https://{self.kbase_host}/#about")
        self.login()
        self.browser.get(f"https://{self.kbase_host}/#{path}")

    def tearDown(self):
        self.browser.close()

    def find_heading(self, level, value):
        # Note that we need to use .= in order to utilize innerText.
        # Generally, the content we are matching may be wrapped in
        # inner elements;
        # we shouldn't care.
        xpath = f'//*[@role="heading" and @aria-level="{level}" and .="{value}"]'
        return self.browser.find_element(By.XPATH, xpath)

    def wait_for_text_xpath(self, xpath, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), value)
        )

    def wait_for_text_by_class(self, class_name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, f'//*[@class="{class_name}"]'), value
            )
        )

    def wait_for_presence(self, element_type, name):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f'//*[@data-k-b-testhook-{element_type}="{name}"]')
            )
        )

    def wait_for_presence_xpath(self, xpath):
        return self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )

    def wait_for_visibility_xpath(self, xpath):
        return self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    def wait_for_element_with_value(self, xpath, text):
        return self.browser.find_element(By.XPATH, f"{xpath}//*[@value='{text}']")

    def wait_for_elements_by_xpath(self, xpath):
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
        )

    def wait_for_title(self, title):
        self.wait.until(expected_conditions.title_is(title))

    def get_parent(self, element):
        return element.find_element(By.XPATH, "..")

    def click(self, xpath):
        element = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()

    def wait_for_table(self, table_xpath, data):
        for row_number, values in enumerate(data):
            row = f"{table_xpath}/tr[{row_number + 1}]"
            for column_number, value in enumerate(values):
                # Skip columns with None value
                if value is None:
                    continue
                col = f"{row}/td[{column_number + 1}]"
                self.wait_for_text_xpath(col, value)

    def wait_for_rotated_table(self, table_xpath, data):
        for row_number, values in enumerate(data):
            row = f"{table_xpath}/tr[{row_number + 1}]"
            for column_number, value in enumerate(values):
                if column_number == 0:
                    col = f"{row}/th"
                else:
                    col = f"{row}/td[{column_number}]"
                self.wait_for_text_xpath(col, value)

    def enter_text(self, xpath, keys):
        control = self.wait_for_visibility_xpath(xpath)
        control.send_keys(keys)

    def push_enter(self, xpath):
        control = self.wait_for_visibility_xpath(xpath)
        control.send_keys(Keys.RETURN)

    def wait_for_labeled_text(self, label, text, xpath=None,):
        label = self.find_element_with_text(label, xpath='//*[@role="label"]')
        label_for = label.get_attribute("for")
        self.wait_for_text_xpath(f'//*[@id="{label_for}"]', text)

    def wait_for_labeled_text2(self, label, text, xpath=None, within=None):
        if within is None:
            within = self.browser

        # Find the label
        label = within.find_element(By.XPATH, f'//*[@role="label" and text()="{label}"]')

        # Find the element pointed to by the "for" attribute.
        # label = self.find_element_with_text(label, xpath='//*[@role="label"]')
        label_for = label.get_attribute("for")

        element = label.find_element(By.XPATH, f'//*[@id="{label_for}" and text()="{text}"]')

        return element

        # self.wait_for_text_xpath(f'//*[@id="{label_for}"]', text)

    def assert_labeled_text(
        self, label, text, comparison="equal", xpath=None, start_from=None
    ):
        if start_from is None:
            start_from = self.browser

        label_element = self.find_element_with_text(
            label, xpath='//*[@role="label"]', start_from=start_from
        )
        label_for = label_element.get_attribute("for")
        text_element = start_from.find_element(By.XPATH, f'//*[@id="{label_for}"]')
        if comparison == "equal":
            self.assertEqual(text_element.text, text)
        elif comparison == "regex":
            self.assertRegex(text_element.text, text)
        # self.wait_for_text_xpath(f'//*[@id="{label_for}"]', text)

    def wait_for_labeled_input(self, label, text, xpath=None):
        label = self.find_element_with_text(label, xpath='//*[@role="label"]')
        label_for = label.get_attribute("for")
        input = self.wait_for_visibility_xpath(f'//input[@id="{label_for}"]')
        self.assertEqual(input.get_attribute("value"), text)

    def assert_table_cell_text(
        self, label, row_number, text, xpath=None, start_from=None
    ):
        # First we locate the header column with the given label, in order to
        # determine the column number.
        header_col = self.find_element_with_text(
            label, xpath="//table/thead/tr/th", start_from=start_from
        )
        row = header_col.find_element(By.XPATH, "./ancestor::tr")
        table = row.find_element(By.XPATH, "./ancestor::table")
        header_cols = row.find_elements(By.XPATH, "th")
        found_col_number = None
        for col_number, col in enumerate(header_cols):
            if col.text == label:
                found_col_number = col_number
                break

        self.assertIsNotNone(found_col_number)

        # Then we can find the cell identified by the column determined above
        # and the row number parameter.
        cell = table.find_element(
            By.XPATH, f"tbody/tr[{row_number}]/td[{found_col_number + 1}]"
        )

        # And finally can assert the value of that cell.
        # TODO: as with other locations, we can apply different comparisons here
        # if we pass in a parameter to control it.
        self.assertEqual(cell.text, text)


    def find_element_containing_text(
        self, text, xpath=None, start_from=None, include_descendents=False
    ):
        if start_from is None:
            start_from = self.browser
            if xpath is None:
                xpath = "//*"
        else:
            if xpath is None:
                xpath = ".//*"

        if include_descendents:
            text_operator = "."
        else:
            text_operator = "text()"

        # this for of contains and text works correctly for cases with multiple text nodes.
        if '"' in text:
            # xpath 1.0 does not support quote escape ("").
            return start_from.find_element(
                By.XPATH, f"{xpath}[contains({text_operator},'{text}')]"
            )
        else:
            return start_from.find_element(
                By.XPATH, f'{xpath}[contains({text_operator},"{text}")]'
            )

    def find_element_with_text(
        self, text, xpath=None, start_from=None, include_descendents=False
    ):
        if start_from is None:
            start_from = self.browser
            if xpath is None:
                xpath = "//*"
        else:
            if xpath is None:
                xpath = ".//*"

        if include_descendents:
            text_operator = "."
        else:
            text_operator = "text()"

        if '"' in text:
            # xpath 1.0 does not support quote escape ("").
            return start_from.find_element(
                By.XPATH, f"{xpath}[{text_operator}='{text}']"
            )
        else:
            return start_from.find_element(
                By.XPATH, f'{xpath}[{text_operator}="{text}"]'
            )

    def find_element_with_this_and_that(
        self, this, that, start_from=None, include_descendents=True
    ):
        this_el = self.find_element_with_text(
            this, start_from=start_from, include_descendents=include_descendents
        )
        parent_el = self.get_parent(this_el)
        return self.find_element_with_text(
            that, start_from=parent_el, include_descendents=include_descendents
        )

    def find_header_with_text(self, text):
        return self.find_element_with_text(
            text, xpath='//*[@role="heading"][@aria-level="1"]'
        )

    def assert_title_old(self, title, include_descendent=False):
        self.find_element_with_text(
            title,
            xpath='//*[@role="heading" and @aria-level="1"]',
            include_descendents=include_descendent,
        )
        self.wait_for_title(f"{title} | KBase")

    def assert_title(self, title, include_descendent=False):
        self.wait_for_text_xpath(
            '//*[@role="heading" and @aria-level="1"]',
            title
#            include_descendents=include_descendent,
        )
        # self.wait_for_title(f"{title} | KBase")

    def wait_for_header_title(self, title, include_descendent=False):
        self.wait_for_text_xpath(
            '//*[@role="heading" and @aria-level="1"]',
            title
        )

    def find_by_text(self, text, start_from=None, xpath="//"):
        if start_from is not None:
            return start_from.find_element(By.XPATH, f'{xpath}*[text()="{text}"]')
        else:
            return self.browser.find_element(By.XPATH, f'{xpath}*[text()="{text}"]')

    def wait_for_attribute_contains(self, start_from, name, value):
        # self.wait.until(expected_conditions.element_attribute_to_include())
        self.wait.until(element_attribute_has_value(start_from, name, value))

    def wait_for_attribute_equal(self, start_from, name, value):
        # self.wait.until(expected_conditions.element_attribute_to_include())
        self.wait.until(element_attribute_is_value(start_from, name, value))

    def assert_aria_button(self, label, start_from=None):
        if start_from is None:
            start_from = self.browser
        return start_from.find_element(
            By.XPATH, f'//*[@role="button"][@aria-label="{label}"]'
        )
