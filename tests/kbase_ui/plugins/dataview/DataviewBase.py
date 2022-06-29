import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.plugins.PluginBase import PluginBase

FUDGE_FACTOR = 0.5


class DataviewBase(PluginBase):
    def wait_for_header(self, title, subtitle, saved_by):
        self.wait_for_text_by_class('MiniOverview-titleCol-title-title', title)
        self.wait_for_text_by_class('MiniOverview-titleCol-title-type', subtitle)
        self.wait_for_text_by_class('MiniOverview-savedCol', saved_by)

    def dataview_tabs_exist(self):
        self.wait_for_text('tab', 'main', 'Data View')
        self.wait_for_text('tab', 'overview', 'Overview')
        self.wait_for_text('tab', 'provenance', 'Provenance')
        self.wait_for_text('tab', 'relatedData', 'Related Data')
        self.wait_for_text('tab', 'linkedSamples', 'Linked Samples')
        self.wait_for_text('tab', 'linkedOntologyTerms', 'Linked Ontology Terms')

    def dataview_click_tab(self, tab_id):
        element = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, f'//*[@data-k-b-testhook-tab="{tab_id}"]')))
        element.click()

    def dataview_click_tab_by_label(self, tab_label):
        """
        Find a tab by its label, then click it.
        """
        element = self.find_element_with_text(tab_label)
        element.click()
        return element

    def assert_rotated_table(self, start_from, table_data):
        for row_number, [expected_label, expected_value] in enumerate(table_data):
            # Find label
            label = self.find_element_with_text(expected_label, start_from=start_from)

            # Row is parent
            row = self.get_parent(label)

            print('row??', row.get_attribute('innerText'))

            # Don't want to do this, but for some reason can't locate the value cell
            # via the combined text across text and dom node children.
            # print('hmm', label, row)
            value_cell = row.find_element(By.XPATH, './td')

            value_cell_content = value_cell.get_attribute('innerText')

            self.assertEqual(value_cell_content, expected_value)

    def assert_data_table(self, start_from, table_data):
        print('[assert_data_table]', start_from.text)
        # print('assert_data_table', start_from, table_data)
        # print('assert_data_table 0')
        # for row_number, column_data in enumerate(table_data):
        #     print('assert_data_table 1', row_number, column_data)
        #     for column_number, column_value in enumerate(column_data):
        #         xpath = f'.//*[@role="table"]//*[@role="row"][position()={row_number + 1}]//[@role="cell"][position()={column_number + 1}]'
        #         print('assert_data_table 2', column_number, column_value, xpath)
        #         cell = start_from.find_element(By.XPATH, xpath)
        # cell_content = cell.get_attribute('innerText')
        # print('cell content', cell, cell.get_attribute('innerHTML'), cell.get_attribute('outerHTML'),
        #       cell.get_attribute('outerText'), cell_content)
        # self.assertRegex(cell_content, column_value)

    def assert_table(self, start_from, table_data):
        for row_number, column_data in enumerate(table_data):
            for column_number, column_value in enumerate(column_data):
                xpath = f'.//table/tbody/tr[{row_number + 1}]/td[{column_number + 1}]'
                cell = start_from.find_element(By.XPATH, xpath)
                cell_content = cell.get_attribute('innerText')
                self.assertEqual(cell_content, column_value)

    def dataview_overview_table(self, cases):
        # Find the summary area, the table should be located within the same
        # parent as the header.

        # Find header.
        header = self.find_element_with_text('Summary')

        summary_container = self.get_parent(header)

        self.assert_rotated_table(summary_container, cases)

        # for row_number, [label, value] in enumerate(cases):
        #     # Find label
        #     label = self.find_element_with_text(label, start_from=summary_container)
        #
        #     # Row is parent
        #     row = self.get_parent(label)
        #
        #     # Don't want to do this, but for some reason can't locate the value cell
        #     # via the combined text across text and dom node children.
        #     # print('hmm', label, row)
        #     value_cell = row.find_element(By.XPATH, './td')
        #
        #     self.assertEqual(value_cell.text, value)

    def open_overview_panel(self, label):
        panel_header = self.find_element_with_text(label)
        panel_header.click()
        time.sleep(FUDGE_FACTOR)

        target_id = panel_header.get_attribute('aria-controls')
        panel_body = self.browser.find_element(By.ID, target_id)
        return panel_body

        # panel_h4 = panel_header.find_element(By.XPATH, './ancestor::h4')
        # print('header??', panel_h4.get_attribute('outerHTML'))
        # panel_heading = panel_header.find_element(By.XPATH, './ancestor::*[@class="panel panel-default"]')
        # print('just header??', panel_heading.get_attribute('innerText'))
        #
        # time.sleep(FUDGE_FACTOR)
        # # panel = panel_header.find_element(By.XPATH, './ancestor::*[contains(@class, "panel")]')
        # panel = panel_header.find_element(By.XPATH, './ancestor::*[@class="panel panel-default"]')
        # panel_body = panel.find_element(By.XPATH, './*[@class="panel-collapse')
        # print('opened panel??', label, panel_header.text, panel.is_displayed())
        # return panel

    def overview_panel(self, panel_number, label):
        # The second column in the overview panel
        column = '//*[@id="tabs123"]/div/div[2]/div/div[2]'

        panel = f'{column}/div/div[{panel_number}]'

        # The header row for the panel (row 1)
        panel_header = f'{panel}/div[1]'

        # The panel toggle button
        panel_button = f'{panel_header}/h4/span'
        # print('overview_panel 1')
        self.wait_for_text_xpath(panel_button, label)
        # print('overview_panel 2')
        self.click(panel_button)
        # print('overview_panel 3')

        # Pause for the tab animation to complete
        time.sleep(FUDGE_FACTOR)

        # The panel body (row 2, wrapped in a div)
        panel_body = f'{panel}/div[2]/div'
        self.wait_for_visibility_xpath(panel_body)

        # print('overview_panel 4')

        # Our assertion within the panel body
        return panel_body

    def close_overview_panel(self, panel_number, label):
        # The second column in the overview panel
        column = '//*[@id="tabs123"]/div/div[2]/div/div[2]'

        panel = f'{column}/div/div[{panel_number}]'

        # The header row for the panel (row 1)
        panel_header = f'{panel}/div[1]'

        # The panel toggle button
        panel_button = f'{panel_header}/h4/span'
        # print('close_panel 1')
        self.wait_for_text_xpath(panel_button, label)
        # print('close_panel 2')
        self.click(panel_button)
        # print('close_panel 3')

    def dataview_navigate(self, object_case):
        self.login_navigate(f'dataview/{object_case["ref"]}')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', f'Data View for {object_case["name"]}')
        self.wait_for_title(f'Data View for {object_case["name"]} | KBase')

        self.switch_to_iframe()

    def dataview_header(self, object_case):
        # The common header
        self.wait_for_header(object_case["name"], object_case["type"], object_case['header']['saved'])

        # Ensure all the tabs are present
        self.dataview_tabs_exist()

    def overview_tab(self, object_case):
        overview_case = object_case['tabs']['overview']

        # Inspect the main overview table.
        # Overview tab
        self.dataview_click_tab_by_label(overview_case['label'])
        self.dataview_overview_table(overview_case['rotated_table'])

        ######
        # Object Info Panel
        ######

        def object_info_panel(case):
            panel = self.open_overview_panel(case['label'])
            expected = case['expected']['rotated_table']
            self.assert_rotated_table(panel, expected)

        object_info_panel(overview_case['panels'][0])

        ######
        # Metadata panel
        ######
        def metadata_panel(case):
            panel = self.open_overview_panel(case['label'])
            print('panel???', panel.get_attribute('innerText'))
            if 'no_data_message' in case['expected']:
                self.find_by_text(case['expected']['no_data_message'], start_from=panel)
            else:
                self.assert_rotated_table(panel, case['expected']['rotated_table'])

        metadata_panel(overview_case['panels'][1])

        ######
        # Versions panel
        ######
        def versions_panel(case):
            panel = self.open_overview_panel(case['label'])
            self.assert_table(panel, case['expected']['table'])

        versions_panel(overview_case['panels'][2])

        ######
        # Referenced by panel
        ######
        def referenced_by_panel(case):
            panel = self.open_overview_panel(case['label'])
            if 'no_data_message' in case['expected']:
                self.find_by_text(case['expected']['no_data_message'], start_from=panel)
            else:
                self.assert_table(panel, case['expected']['table'])

        referenced_by_panel(overview_case['panels'][3])

        ######
        # References panel
        ######
        def references_panel(case):
            panel = self.open_overview_panel(case['label'])
            if 'no_data_message' in case['expected']:
                self.find_by_text(case['expected']['no_data_message'], start_from=panel)
            else:
                self.assert_table(panel, case['expected']['table'])

        references_panel(overview_case['panels'][4])

    def common_expectations(self, expectations, start_from=None):
        for expectation in expectations:
            if expectation['type'] == 'rotated_table':
                self.assert_rotated_table(start_from, expectation['data'])
            elif expectation['type'] == 'table':
                self.assert_table(start_from, expectation['data'])
            elif expectation['type'] == 'data-table':
                self.assert_data_table(start_from, expectation['data'])
            elif expectation['type'] == 'text':
                if 'contains' in expectation:
                    for expected_text in expectation['contains']:
                        self.find_element_containing_text(expected_text, start_from=start_from)

    def dataview_tab(self, object_case):
        dataview_case = object_case['tabs']['dataview']
        tab_label = self.dataview_click_tab_by_label(dataview_case['label'])
        tabset = tab_label.find_element(By.XPATH, './ancestor::*[@role="tablist"]')

        # self.dataview_click_tab('main')
        # dataview_tab_pane = f'//*[@data-k-b-testhook-tabpane="main"]'

        # def select_tabx(tab_number, click=True):
        #     case = dataview_case['tabs'][tab_number - 1]
        #     tab = f'{dataview_tab_pane}//ul[@class="nav nav-tabs"]/li[{tab_number}]'
        #     self.wait_for_text_xpath(tab, case['title'])
        #     if click:
        #         tab_button = f'{tab}/a'
        #         self.click(tab_button)
        #     tab_pane = f'{dataview_tab_pane}//div[@class="tab-content"]/div[{tab_number}]'
        #     return [case, tab_pane]

        def select_tab(tab_label, case, start_from=None, click=True):
            return self.dataview_click_tab_by_label(case['label'])

        def select_panel(panel_number):
            panel_title = self.find_element_with_text(case['label'])
            panel = panel_title.find_element(By.XPATH, './ancestor::*[contains(@class,"panel")]')
            return panel
            # panel = f'{dataview_tab_pane}//div[@data-element="panel"]/div[{panel_number}]'
            # return [case, panel]

        if 'tabs' in dataview_case:
            for tab_number, tab_case in enumerate(dataview_case['tabs'], start=1):
                case = dataview_case['tabs'][tab_number - 1]
                select_tab(tab_case['label'], case, click=False if tab_number == 1 else True)
                if 'sections' in tab_case:
                    for section_case in tab_case['sections']:
                        section_heading = self.find_element_with_text(section_case['title'])
                        section_body = section_heading.find_element(By.XPATH, './ancestor::section[1]')
                        self.common_expectations(section_case['expectations'], start_from=section_body)
        elif 'panels' in dataview_case:
            for panel_number, tab in enumerate(dataview_case['panels'], start=1):
                case = dataview_case['panels'][panel_number - 1]
                panel = select_panel(case)
                self.common_expectations(case['expectations'], start_from=panel)
        # elif 'expectations' in dataview_case:
        #     common_expectations(dataview_tab_pane, dataview_case['expectations'])
        elif 'not_supported' in dataview_case:
            message = 'This object does not have a specific visualization'
            self.find_element_with_text(message, start_from=tabset)
            # self.wait_for_text_xpath(tabset, message)

    def auth_blocked_plugin(self, plugin_path):
        self.navigate(plugin_path)

        self.switch_to_iframe()

        request_path = self.kbase_testhook(
            [['plugin', 'auth2-client'], ['component', 'login-view'], ['field', 'requested-path']])
        self.wait_for_text_xpath(request_path, plugin_path)
