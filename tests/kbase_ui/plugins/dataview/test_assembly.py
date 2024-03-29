from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewAssemblyTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/17/1',
            'name': 'GCF_001223685.1_assembly',
            'type': 'KBaseGenomeAnnotations.Assembly-6.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'panels': [
                        {
                            'label': 'Summary',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['Number of Contigs', '26'],
                                        ['Total GC Content', '31.36%'],
                                        ['Total Length', '1,700,953 bp'],
                                        ['External Source', 'n/a'],
                                        ['External Source ID', 'n/a'],
                                        ['Source Origination Date', 'n/a'],
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'contigs',
                            'label': 'Contigs',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['1', 'NZ_CUHU01000001.1', '420,607', '30.96'],
                                        ['2', 'NZ_CUHU01000002.1', '271,771', '32.11'],
                                        ['3', 'NZ_CUHU01000003.1', '270,378', '31.29'],
                                        ['4', 'NZ_CUHU01000004.1', '182,740', '32.12'],
                                        ['5', 'NZ_CUHU01000005.1', '163,595', '31.59'],
                                    ]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'name': 'overview',
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'Assembly'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/17/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseGenomeAnnotations'],
                                    ['Type', 'Assembly'],
                                    ['Type Version', '6.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/legacy/dataview/45593/17/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
                                    ['GC content', '0.31365'],
                                    ['Size', '1700953'],
                                    ['N Contigs', '26'],
                                    ['MD5', '567b906a2ceda25894da7ebdcfc48c65']
                                ]
                            }
                        },
                        {
                            'label': 'Versions',
                            'expected': {
                                'table': [
                                    ['v1', 'Saved on Jun 6, 2022 by kbaseuitest']
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
                                    [None, 'GCF_001223685.1_assembly', 'Assembly', 'May 20, 2018', 'qzhang']
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
