from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewContigSetTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/8/8',
            'name': 'Rhodobacter_CACIA_14H1_contigs',
            'type': 'KBaseGenomes.ContigSet-2.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'expectations': [
                        {
                            'type': 'table',
                            'data': [
                                ['1', 'NODE_48_length_21448_cov_4.91263_ID_95', '21,448', '∅'],
                                ['2', 'NODE_154_length_9553_cov_5.05327_ID_307', '9,553', '∅'],
                                ['3', 'NODE_25_length_29402_cov_4.90142_ID_49', '29,402', '∅'],
                                ['4', 'NODE_185_length_8164_cov_5.03663_ID_369', '8,164', '∅'],
                                ['5', 'NODE_39_length_23133_cov_4.96429_ID_77', '23,133', '∅'],
                            ]
                        }
                    ]
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'ContigSet'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/8/8']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '8'],
                                    ['Type Module', 'KBaseGenomes'],
                                    ['Type', 'ContigSet'],
                                    ['Type Version', '2.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/8/8']
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
                                    ['v8', 'Saved on Jun 3, 2022 by kbaseuitest'],
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
                                    [None, 'Rhodobacter_CACIA_14H1_contigs', 'ContigSet', 'Feb 6, 2015',
                                     'kbasetest']
                                ]
                            }
                        }
                    ]
                }
            },

        }

        self.dataview_navigate(object_case)
        self.dataview_header(object_case)
        self.dataview_tab(object_case)
        self.overview_tab(object_case)
