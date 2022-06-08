from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewMediaTest(DataviewBase):
    def media_overview_table_row(self, row_id, value):
        self.wait.until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH,
             f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tabpane="overview"]//*[@data-k-b-testhook-field="{row_id}"]'),
            value))

    def media_tab_pane(self, tab_id):
        return f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tabpane="{tab_id}"]'

    def media_click_tab(self, tab_id):
        element = self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tab="{tab_id}"]')))
        element.click()

    def test_authenticated_media(self):
        object_case = {
            'ref': '45593/2/8',
            'name': 'Rsp-minimal',
            'type': 'KBaseBiochem.Media-1.0',
            'header': {
                'saved': 'Saved Jan 6, 2020 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'title': 'Overview',
                    'tabs': [
                        {
                            'title': 'Overview',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['ID', 'kbaseuitest:narrative_1578347520053/Rsp-minimal'],
                                        ['Object type', 'KBaseBiochem.Media-1.0'],
                                        ['Owner', 'kbaseuitest'],
                                        ['Version', '8'],
                                        ['Mod-date', '2020-01-06T21:53:38+0000']
                                    ]
                                }
                            ]
                        },
                        {
                            'title': 'Media compounds',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['cpd00001', 'H2O', 'H2O', '0', '-100', '100'],
                                        ['cpd00007', 'O2', 'O2', '0', '-100', '100'],
                                        ['cpd00009', 'Phosphate', 'HO4P', '-2', '-100', '5'],
                                        ['cpd00011', 'CO2', 'CO2', '0', '-100', '100'],
                                        ['cpd00013', 'NH3', 'H4N', '1', '-100', '5'],
                                    ]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'name': 'overview',
                    'tabs': [
                        ['Type', 'Media'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jan 6, 2020 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/2/8']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'data': [
                                    ['Object Version', '8'],
                                    ['Type Module', 'KBaseBiochem'],
                                    ['Type', 'Media'],
                                    ['Type Version', '1.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jan 6, 2020 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/2/8']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'no_data_message': 'no metadata for this object'
                            }
                        },
                        {
                            'label': 'Versions',
                            'expected': {
                                'data': [
                                    ['v1', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v2', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v3', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v4', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v5', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v6', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v7', 'Saved on Jan 6, 2020 by kbaseuitest'],
                                    ['v8', 'Saved on Jan 6, 2020 by kbaseuitest']
                                ]
                            }
                        },
                        {
                            'label': 'Referenced by',
                            'expected': {
                                'no_data_message': 'No other data references this data object.'
                            }
                        },
                        {
                            'label': 'References',
                            'expected': {
                                'no_data_message': 'This object does not reference any other data object.'
                            }
                        }
                    ]
                }
            }
        }

        self.dataview_navigate(object_case)
        self.dataview_header(object_case)
        self.dataview_tab(object_case)
        self.overview_tab(object_case)
