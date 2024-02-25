from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.TestBase import TestBase


class KBaseUIBase(TestBase):
    def kbase_testhook(self, testhooks):
        path = []
        for [name, value] in testhooks:
            path.append(f'//*[@data-k-b-testhook-{name}="{value}"]')
        return "".join(path)

    def wait_for_panel_title(self, name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, f'//*[@data-k-b-testhook-panel="{name}"]/h2'), value
            )
        )

    def switch_to_iframe(self):
        iframe = self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//iframe[@data-k-b-testhook-iframe="plugin-iframe"]')
            )
        )
        self.browser.switch_to.frame(iframe)

    def wait_for_text(self, element_type, name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, f'//*[@data-k-b-testhook-{element_type}="{name}"]'), value
            )
        )

    def wait_for_label(self, name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, f'//span[@data-k-b-testhook-label="{name}"]'), value
            )
        )

    def wait_for_titles(self, title):
        self.wait_for_text("component", "title", title)
        self.wait_for_title(f"{title} | KBase")

    def switch_to_kbase_ui_iframe(self):
        iframe = self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//iframe')
            )
        )
        self.browser.switch_to.frame(iframe)

    def auth_blocked(self, plugin_path, name):
        self.navigate(plugin_path)
        self.navigate(plugin_path)
        self.wait_for_title('KBase: KBase Sign In')
        self.wait_for_header_title('KBase Sign In')
        self.switch_to_kbase_ui_iframe()
        self.wait_for_text_xpath('//h2', 'Welcome to KBase')
        self.wait_for_text_xpath('//*[@role="heading"]', 'Sign In Required')
        self.wait_for_text_xpath('//*[@role="region"]', f'Sign In is required to access {name}.')

    def find_well(self, heading_text, start_from=None):
        """
        Finds and returns a Well with the given heading title
        """
        if start_from is None:
            start_from = self.browser

        xpath = f'//*[@role="article"]/*[@role="heading" and text()="{heading_text}"]'

        heading = start_from.find_element(
            By.XPATH, xpath
        )
        return heading.find_element(By.XPATH, './ancestor::*[@role="article"][1]')

    def assert_table2(self, header=None, rows=None, row_count=None, start_from=None):
        if start_from is None:
            start_from = self.browser
