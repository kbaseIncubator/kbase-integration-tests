from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewReferenceAssemblyTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/9/8',
            'name': 'rhodobacter_CACIA14H1.reference',
            'type': 'KBaseAssembly.ReferenceAssembly-1.1',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'expectations': [
                        {
                            'type': 'rotated_table',
                            'data': [
                                ['Source file name', 'rhodobacter_CACIA14H1.fasta']
                            ]
                        }
                    ]
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'ReferenceAssembly'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/9/8']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '8'],
                                    ['Type Module', 'KBaseAssembly'],
                                    ['Type', 'ReferenceAssembly'],
                                    ['Type Version', '1.1'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/9/8']
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
                                'table': [
                                    ['v1', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v2', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v3', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v4', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v5', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v6', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v7', 'Saved on Jun 3, 2022 by kbaseuitest'],
                                    ['v8', 'Saved on Jun 3, 2022 by kbaseuitest']
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
                                        None, 'rhodobacter_CACIA14H1.reference', 'ReferenceAssembly',
                                        'Feb 6, 2015', 'kbasetest'
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
