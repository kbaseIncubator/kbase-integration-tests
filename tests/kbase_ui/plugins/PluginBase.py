from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class PluginBase(KBaseUIBase):

    def switch_to_kbase_ui_plugin_iframe(self):
        iframe = self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//iframe')
            )
        )
        self.browser.switch_to.frame(iframe)

        iframe = self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//iframe')
            )
        )
        self.browser.switch_to.frame(iframe)

    def auth_blocked_plugin(self, plugin_path, plugin_name):
        self.navigate(plugin_path)
        self.wait_for_title('KBase: KBase Sign In')
        self.wait_for_header_title('KBase Sign In')
        self.switch_to_kbase_ui_iframe()
        self.wait_for_text_xpath('//h2', 'Welcome to KBase')
        self.wait_for_text_xpath('//*[@role="heading"]', 'Sign In Required')
        self.wait_for_text_xpath('//*[@role="region"]', f'Sign In is required to access {plugin_name}.')


        # # TODO: visually based rather than using hidden testing hooks
        # request_path = self.kbase_testhook(
        #     [['plugin', 'auth2-client'], ['field', 'requested-path']])
        # self.wait_for_text_xpath(request_path, plugin_path)

    def assert_table(self, start_from, table_data):
        for row_number, column_data in enumerate(table_data):
            for column_number, column_value in enumerate(column_data):
                xpath = f'.//table/tbody/tr[{row_number + 1}]/td[{column_number + 1}]'
                cell = start_from.find_element(By.XPATH, xpath)
                cell_content = cell.get_attribute('innerText')
                self.assertEqual(cell_content, column_value)

    def assert_data_table(self, start_from, table_data):
        for row_number, column_data in enumerate(table_data):
            # skip rows with None as the expected data.
            if column_data is None:
                continue
            for column_number, column_value in enumerate(column_data):
                if column_value is None:
                    # skip null values for now.
                    continue
                xpath = f'.//*[@role="table"]//*[@role="row"][{row_number + 1}]//*[@role="cell"][{column_number + 1}]'
                cell = start_from.find_element(By.XPATH, xpath)
                cell_content = cell.get_attribute('innerText')
                self.assertEqual(cell_content, column_value)

    def assert_table2(self, header=None, rows=None, row_count=None, start_from=None):
        if start_from is None:
            start_from = self.browser

        def assert_header():
            for column_number, column_value in enumerate(header):
                xpath = f'.//table/thead/tr[1]/th[{column_number + 1}]'
                cell = start_from.find_element(By.XPATH, xpath)
                cell_content = cell.get_attribute('innerText')
                self.assertEqual(cell_content, column_value)

        def assert_row_count():
            rows = start_from.find_elements(By.XPATH, './/table/tbody/tr')
            self.assertEqual(len(rows), row_count)

        def assert_rows():
            for row_number, column_data in enumerate(rows):
                for column_number, column_value in enumerate(column_data):
                    xpath = f'.//table/tbody/tr[{row_number + 1}]/td[{column_number + 1}]'
                    cell = start_from.find_element(By.XPATH, xpath)
                    cell_content = cell.get_attribute('innerText')
                    self.assertEqual(cell_content, column_value)

        if header is not None:
            assert_header()

        if row_count is not None:
            assert_row_count()

        if rows is not None:
            assert_rows();

    def find_panel(self, heading_text, start_from=None):
        if start_from is None:
            start_from = self.browser
        heading_label = self.find_element_with_text(heading_text,
                                                    xpath=f'//*[@role="article"]/*[@role="heading"]//*',
                                                    include_descendents=False,
                                                    start_from=start_from)
        panel = heading_label.find_element(By.XPATH, './ancestor::*[@role="article"][1]')
        return panel
