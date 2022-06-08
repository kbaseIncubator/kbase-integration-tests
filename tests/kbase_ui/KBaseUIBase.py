from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.TestBase import TestBase


class KBaseUIBase(TestBase):
    def kbase_testhook(self, testhooks):
        path = []
        for [name, value] in testhooks:
            path.append(f'//*[@data-k-b-testhook-{name}="{value}"]')
        return ''.join(path)

    def wait_for_panel_title(self, name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, f'//*[@data-k-b-testhook-panel="{name}"]/h2'),
                                                              value))

    def switch_to_iframe(self):
        iframe = self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//iframe[@data-k-b-testhook-iframe="plugin-iframe"]')))
        self.browser.switch_to.frame(iframe)

    def wait_for_text(self, element_type, name, value):
        self.wait.until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, f'//*[@data-k-b-testhook-{element_type}="{name}"]'), value))

    def wait_for_label(self, name, value):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, f'//span[@data-k-b-testhook-label="{name}"]'),
                                                              value))

    def wait_for_presence(self, element_type, name):
        return self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, f'//*[@data-k-b-testhook-{element_type}="{name}"]')))

    def wait_for_titles(self, title):
        self.wait_for_text('component', 'title', title)
        self.wait_for_title(f'{title} | KBase')
