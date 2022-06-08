from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewFeatureSetTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/21/1',
            'name': 'test_FeatureSet',
            'type': 'KBaseCollections.FeatureSet-4.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'not_supported': True
                },
                'overview': {
                    'name': 'overview',
                    'tabs': [
                        ['Type', 'FeatureSet'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/21/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'data': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseCollections'],
                                    ['Type', 'FeatureSet'],
                                    ['Type Version', '4.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/21/1']
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
                                    ['v1', 'Saved on Jun 6, 2022 by kbaseuitest']
                                ]
                            }
                        },
                        {
                            'label': 'Referenced by',
                            'expected': {
                                'data': [
                                    [
                                        'kb_FeatureSetUtils_report_146eb944-af02-4eea-9fc1-f75e1da10e71',
                                        'Report',
                                        'Jun 6, 2022',
                                        'kbaseuitest'
                                    ],
                                ]
                            }
                        },
                        {
                            'label': 'References',
                            'expected': {
                                'data': [

                                    [
                                        'Prochlorococcus_marinus_str._AS9601',
                                        'Genome',
                                        'Jun 6, 2022',
                                        'kbaseuitest'
                                    ],
                                    [
                                        'Prochlorococcus_marinus_str._AS9601',
                                        'Genome',
                                        'Jun 6, 2022',
                                        'kbaseuitest'
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
