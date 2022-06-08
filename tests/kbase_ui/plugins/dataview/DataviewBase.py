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

    def dataview_overview_table(self, cases):
        def overview_table_label(row):
            return f'//*[@id="tabs123"]/div/div[2]/div/div[1]/table/tbody/tr[{row + 1}]/th'

        def overview_table_value(row):
            return f'//*[@id="tabs123"]/div/div[2]/div/div[1]/table/tbody/tr[{row + 1}]/td'

        for row_number, [label, value] in enumerate(cases):
            self.wait.until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, overview_table_label(row_number)), label))

            self.wait.until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, overview_table_value(row_number)), value))

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
        self.dataview_click_tab('overview')

        self.dataview_overview_table(overview_case['tabs'])

        ######
        # Object Info Panel
        ######
        def object_info_panel(panel_number, case):
            panel = self.overview_panel(panel_number, case['label'])
            expected = case['expected']['data']
            for row_number, [label, value] in enumerate(expected):
                object_info_row = f'{panel}//table/tbody/tr[{row_number + 1}]'
                label_cell = f'{object_info_row}/th'
                value_cell = f'{object_info_row}/td'
                self.wait.until(expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, label_cell), label))
                self.wait.until(expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, value_cell), value))

        object_info_panel(1, overview_case['panels'][0])

        ######
        # Metadata panel
        ######
        def metadata_panel(panel_number, case):
            panel = self.overview_panel(panel_number, case['label'])
            if 'no_data_message' in case['expected']:
                self.wait_for_text_xpath(panel, case['expected']['no_data_message'])
            else:
                for row_number, [label, value] in enumerate(case['expected']['data']):
                    # row = self.wait_for_presence_xpath(f'{panel}//table/tbody/tr')
                    # self.actions.move_to_element(row).perform()
                    self.wait_for_text_xpath(f'{panel}//table/tbody/tr[{row_number + 1}]/th', label)
                    self.wait_for_text_xpath(f'{panel}//table/tbody/tr[{row_number + 1}]/td', value)

        metadata_panel(2, overview_case['panels'][1])

        ######
        # Versions panel
        ######
        def versions_panel(panel_number, case):
            panel = self.overview_panel(panel_number, case['label'])
            for row_number, column_data in enumerate(case['expected']['data']):
                for column_number, data in enumerate(column_data):
                    self.wait_for_text_xpath(f'{panel}//table/tbody/tr[{row_number + 1}]/td[{column_number + 1}]', data)

        versions_panel(3, overview_case['panels'][2])

        ######
        # Referenced by panel
        ######
        def referenced_by_panel(panel_number, case):
            panel = self.overview_panel(panel_number, case['label'])
            if 'no_data_message' in case['expected']:
                self.wait_for_text_xpath(panel, case['expected']['no_data_message'])
            else:
                for row_number, column_data in enumerate(case['expected']['data']):
                    row = f'{panel}//table/tbody/tr[{row_number + 1}]'
                    for column_number, data in enumerate(column_data):
                        self.wait_for_text_xpath(f'{row}/td[{column_number + 1}]', data)

        referenced_by_panel(4, overview_case['panels'][3])

        ######
        # References panel
        ######
        def references_panel(panel_number, case):
            panel = self.overview_panel(panel_number, case['label'])

            time.sleep(FUDGE_FACTOR)
            if 'no_data_message' in case['expected']:
                self.wait_for_text_xpath(panel, case['expected']['no_data_message'])
            else:
                for row_number, column_data in enumerate(case['expected']['data']):
                    row = f'{panel}//table/tbody/tr[{row_number + 1}]'
                    for column_number, data in enumerate(column_data):
                        self.wait_for_text_xpath(f'{row}/td[{column_number + 1}]', data)

        references_panel(5, overview_case['panels'][4])

    def dataview_tab(self, object_case):
        self.dataview_click_tab('main')
        dataview_tab_pane = f'//*[@data-k-b-testhook-tabpane="main"]'
        dataview_case = object_case['tabs']['dataview']

        def select_tab(tab_number, click=True):
            case = dataview_case['tabs'][tab_number - 1]
            tab = f'{dataview_tab_pane}//ul[@class="nav nav-tabs"]/li[{tab_number}]'
            self.wait_for_text_xpath(tab, case['title'])
            if click:
                tab_button = f'{tab}/a'
                self.click(tab_button)
            tab_pane = f'{dataview_tab_pane}//div[@class="tab-content"]/div[{tab_number}]'
            return [case, tab_pane]

        def select_panel(panel_number):
            case = dataview_case['panels'][panel_number - 1]
            panel = f'{dataview_tab_pane}//div[@data-element="panel"]/div[{panel_number}]'
            return [case, panel]

        def common_expectations(xpath, expectations):
            for expectation in expectations:
                if expectation['type'] == 'rotated_table':
                    table_xpath = f'{xpath}//table/tbody'
                    self.wait_for_rotated_table(table_xpath, expectation['data'])
                elif expectation['type'] == 'table':
                    table_xpath = f'{xpath}//table/tbody'
                    self.wait_for_table(table_xpath, expectation['data'])
                elif expectation['type'] == 'text':
                    text_xpath = f'{xpath}//{expectation["xpath"]}'
                    self.wait_for_text_xpath(text_xpath, expectation['data'])

        if 'tabs' in dataview_case:
            for tab_number, tab in enumerate(dataview_case['tabs'], start=1):
                case, tab_pane = select_tab(tab_number, click=False if tab_number == 1 else True)
                common_expectations(tab_pane, case['expectations'])
        elif 'panels' in dataview_case:
            for panel_number, tab in enumerate(dataview_case['panels'], start=1):
                case, panel = select_panel(panel_number)
                common_expectations(panel, case['expectations'])
        elif 'expectations' in dataview_case:
            common_expectations(dataview_tab_pane, dataview_case['expectations'])
        elif 'not_supported' in dataview_case:
            message = 'This object does not have a specific visualization'
            self.wait_for_text_xpath(dataview_tab_pane, message)

    def auth_blocked_plugin(self, plugin_path):
        self.navigate(plugin_path)

        self.switch_to_iframe()

        request_path = self.kbase_testhook(
            [['plugin', 'auth2-client'], ['component', 'login-view'], ['field', 'requested-path']])
        self.wait_for_text_xpath(request_path, plugin_path)
