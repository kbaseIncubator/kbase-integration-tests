import os
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

DEFAULT_TIMEOUT = 30  # seconds


class TestBase(unittest.TestCase):
    def __init__(self, *args):
        self.kbase_host = self.kbase_host_from_env()
        self.run_headless = self.get_headless_from_env()
        self.run_insecure = os.environ.get('INSECURE') == 't'
        self.run_browser = os.environ.get('BROWSER') or 'chrome'
        if self.run_browser not in ['chrome', 'firefox']:
            raise ValueError((
                'The "BROWSER" environment variable may only be set to "chrome" or "firefox";'
                f' "{self.run_browser}" is not a supported browser; it defaults to "chrome"'))
        self.timeout = self.get_timeout_from_env()
        super().__init__(*args)

    def get_headless_from_env(self):
        headless_env = os.environ.get('HEADLESS') or "t"
        if headless_env == 't':
            return True
        if headless_env == 'f':
            return False
        raise ValueError((
            'The "HEADLESS" environment variable must be "t", "f" or omitted; '
            f'it was set to "{headless_env}"; '
            'it defaults to "t"'))

    def get_timeout_from_env(self):
        timeout_env = os.environ.get('TIMEOUT')
        if timeout_env is None:
            return DEFAULT_TIMEOUT
        try:
            return float(timeout_env)
        except ValueError as ve:
            raise ValueError((
                'The "TIMEOUT" environment variable must be a number number; '
                f'"{timeout_env}" is no good; it defaults to "30"'))

    def kbase_host_from_env(self):
        env = os.environ.get('KBASE_ENV')
        if env is None:
            return 'ci.kbase.us'
        if env in ['ci', 'next', 'narrative-dev', 'appdev']:
            return f'{env}.kbase.us'
        if env == 'prod':
            return 'kbase.us'
        raise ValueError(
            ('The "KBASE_ENV" environment variable is incorrect; '
             f'"{env}" is not a recognized KBase deployment environment; '
             'supported environments are "ci", "next", "appdev", "narrative-dev" and "prod"; '
             'it defaults to "ci"'))

    def setup_chrome(self):
        chrome_options = Options()
        if self.run_headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')

        # If a CORS error is thrown for external apis (e.g. genome publications), enabling
        # these lines may reveal an underlying error (as many sites don't have cors set up
        # correctly for error responses.)
        # chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--disable-site-isolation-trials")

        if self.run_insecure:
            chrome_options.add_argument('--ignore-certificate-errors')

        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def setup_firefox(self):
        firefox_options = FirefoxOptions()

        if self.run_headless:
            firefox_options.add_argument('--headless')
        if self.run_insecure:
            firefox_options.accept_insecure_certs = True

        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                         options=firefox_options)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.actions = ActionChains(self.browser)

    def setUp(self):
        if self.run_browser == 'chrome':
            self.setup_chrome()
        elif self.run_browser == 'firefox':
            self.setup_firefox()

    def login(self):
        self.browser.delete_all_cookies()
        self.browser.add_cookie({
            'name': 'kbase_session',
            'path': '/',
            'value': os.environ.get('KBASE_TOKEN')
        })
        self.wait_for_presence('menu', 'signed-in')

    def logout(self):
        self.browser.delete_all_cookies()

    def navigate(self, path):
        self.browser.get(f'https://{self.kbase_host}/#{path}')

    def login_navigate(self, path):
        self.browser.get(f'https://{self.kbase_host}/#about')
        self.login()
        self.browser.get(f'https://{self.kbase_host}/#{path}')

    def tearDown(self):
        self.browser.close()

    def wait_for_text_xpath(self, xpath, value):
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), value))

    def wait_for_text_by_class(self, class_name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, f'//*[@class="{class_name}"]'), value))

    def wait_for_presence_xpath(self, xpath):
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def wait_for_visibility_xpath(self, xpath):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_element_containing_text(self, xpath, text):
        return self.browser.find_element(By.XPATH, f"{xpath}//*[contains(text(), '{text}')]")

    def wait_for_element_with_text(self, xpath, text):
        return self.browser.find_element(By.XPATH, f"{xpath}//*[text()='{text}']")

    def wait_for_element_with_value(self, xpath, text):
        return self.browser.find_element(By.XPATH, f"{xpath}//*[@value='{text}']")

    def wait_for_elements_by_xpath(self, xpath):
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath)))

    def wait_for_title(self, title):
        self.wait.until(expected_conditions.title_is(title))

    def get_parent(self, element):
        return element.find_element(By.XPATH, '..')

    def click(self, xpath):
        element = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def wait_for_table(self, table_xpath, data):
        for row_number, values in enumerate(data):
            row = f'{table_xpath}/tr[{row_number + 1}]'
            for column_number, value in enumerate(values):
                # Skip columns with None value
                if value is None:
                    continue
                col = f'{row}/td[{column_number + 1}]'
                self.wait_for_text_xpath(col, value)

    def wait_for_rotated_table(self, table_xpath, data):
        for row_number, values in enumerate(data):
            row = f'{table_xpath}/tr[{row_number + 1}]'
            for column_number, value in enumerate(values):
                if column_number == 0:
                    col = f'{row}/th'
                else:
                    col = f'{row}/td[{column_number}]'
                self.wait_for_text_xpath(col, value)

    def enter_text(self, xpath, keys):
        control = self.wait_for_visibility_xpath(xpath)
        control.send_keys(keys)

    def push_enter(self, xpath):
        control = self.wait_for_visibility_xpath(xpath)
        control.send_keys(Keys.RETURN)

    def wait_for_labeled_text(self, xpath, label, text):
        label = self.wait_for_element_with_text(xpath, label)
        label_for = label.get_attribute('for')
        self.wait_for_text_xpath(f'//*[@id="{label_for}"]', text)

    def wait_for_labeled_input(self, xpath, label, text):
        label = self.wait_for_element_with_text(xpath, label)
        label_for = label.get_attribute('for')
        input = self.wait_for_visibility_xpath(f'//input[@id="{label_for}"]')
        self.assertEqual(input.get_attribute('value'), text)

    def wait_for_table_cell_text(self, xpath, label, row_number, text):
        header_col = self.wait_for_element_with_text(xpath, label)
        row = header_col.find_element(By.XPATH, './ancestor::tr')
        table = row.find_element(By.XPATH, './ancestor::table')
        header_cols = row.find_elements(By.XPATH, 'th')
        found_col_number = None
        for col_number, col in enumerate(header_cols):
            if col.text == label:
                found_col_number = col_number
                break

        self.assertIsNotNone(found_col_number)

        # row = self.wait_for_elements_by_xpath(f'{header_col.generateXPATH}')
        # table = header_col.find_element(By.XPATH, f'./ancestor::table/tbody/tr')
        cell = table.find_element(By.XPATH, f'tbody/tr[{row_number}]/td[{found_col_number + 1}]')
        self.assertEqual(cell.text, text)
