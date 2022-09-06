from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewExpressionMatrixTest(DataviewBase):
    # def media_overview_table_row(self, row_id, value):
    #     self.wait.until(expected_conditions.text_to_be_present_in_element(
    #         (By.XPATH,
    #          f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tabpane="overview"]//*[@data-k-b-testhook-field="{row_id}"]'),
    #         value))
    #
    # def media_tab_pane(self, tab_id):
    #     return f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tabpane="{tab_id}"]'
    #
    # def media_click_tab(self, tab_id):
    #     element = self.wait.until(expected_conditions.presence_of_element_located(
    #         (By.XPATH, f'//*[@data-k-b-testhook-tabpane="main"]//*[@data-k-b-testhook-tab="{tab_id}"]')))
    #     element.click()

    def test_authenticated_media(self):
        object_case = {
            'ref': '45593/6/1',
            'name': 'SomeFakeData',
            'type': 'KBaseFeatureValues.ExpressionMatrix-1.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'not_supported': True
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'ExpressionMatrix'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/6/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseFeatureValues'],
                                    ['Type', 'ExpressionMatrix'],
                                    ['Type Version', '1.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/6/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
                                    ['scale', '1.0'],
                                    ['feature_count', '4297'],
                                    ['condition_count', '16'],
                                    ['type', 'log-ratio'],
                                    ['Genome', '899/6/2']
                                ]
                            }
                        },
                        {
                            'label': 'Versions',
                            'expected': {
                                'table': [
                                    ['v1', 'Saved on Jun 3, 2022 by kbaseuitest']
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
                                'data_table': [
                                    [
                                        None,
                                        'Escherichia_coli_str_K-12_substr_MG1655_NCBI',
                                        'Genome',
                                        'Jul 29, 2015',
                                        'rsutormin'
                                    ],
                                    [
                                        None,
                                        'SomeFakeData',
                                        'ExpressionMatrix',
                                        'Aug 12, 2015',
                                        'kbasetest'
                                    ]
                                ]
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
