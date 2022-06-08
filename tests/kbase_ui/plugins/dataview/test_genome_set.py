from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenomeSetTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/7/1',
            'name': 'Rhodobacter_external_genomes',
            'type': 'KBaseSearch.GenomeSet-2.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'title': 'Data View',
                    'tabs': [
                        {
                            'title': 'Overview',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['ID', 'kbaseuitest:narrative_1578347520053/Rhodobacter_external_genomes'],
                                        ['Object type', 'KBaseSearch.GenomeSet-2.0'],
                                        ['Owner', 'kbaseuitest'],
                                        ['Version', '1'],
                                        ['Mod-date', '2022-06-03T23:22:58+0000']
                                    ]
                                }
                            ]
                        },
                        {
                            'title': 'Genomes',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['Rhodobacter_CACIA_14H1'],
                                        ['Rhodobacter_sphaeroides_2.4.1'],
                                        ['Rhodobacter_sphaeroides_2.4.1_KBase']
                                    ]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'name': 'overview',
                    'tabs': [
                        ['Type', 'GenomeSet'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/7/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'data': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseSearch'],
                                    ['Type', 'GenomeSet'],
                                    ['Type Version', '2.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/7/1']
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
                                'data': [
                                    [
                                        'Rhodobacter_CACIA_14H1',
                                        'Genome',
                                        'Jan 15, 2015',
                                        'kbasetest'
                                    ],
                                    [
                                        'Rhodobacter_sphaeroides_2.4.1',
                                        'Genome',
                                        'Jan 15, 2015',
                                        'kbasetest'
                                    ],
                                    [
                                        'Rhodobacter_sphaeroides_2.4.1_KBase',
                                        'Genome',
                                        'Jan 15, 2015',
                                        'kbasetest'
                                    ],
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
