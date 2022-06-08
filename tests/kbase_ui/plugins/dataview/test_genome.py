from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenomeTest(DataviewBase):
    def test_authenticated_rhodobacter(self):
        object_case = {
            'ref': '45593/5/1',
            'name': 'Rhodobacter_sphaeroides_2.4.1',
            'type': 'KBaseGenomes.Genome-7.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'panels': [
                        {
                            'title': 'Overview',
                            'expectations': [
                                {
                                    'type': 'rotated_table',
                                    'data': [
                                        ['Name', 'Rhodobacter sphaeroides 2.4.1'],
                                        ['KBase Genome ID', 'Rhodobacter_sphaeroides_2.4.1'],
                                        ['Domain', 'Bacteria'],
                                        ['DNA Length', '4,602,977'],
                                        ['Source ID', 'NCBI: NCBI'],
                                        ['Number of Contigs', '7'],
                                        ['GC Content', '68.79 %'],
                                        ['Genetic Code', '11'],
                                        ['Number of features', '4,347']
                                    ]
                                },
                            ]
                        },
                        {
                            'title': 'Publications',
                            'notes': [
                                'Will trigger 429 (too many requests) if tests run too often'
                            ],
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['Microorganisms',
                                         'Wang H, Sha X, Li R, Li Y, Khaleque HN, Zhang Y, Bohu T, Bai Z, Zhuang X',
                                         'Comparative Genome Analysis Provides Molecular Evidence for Reclassification of the Photosynthetic Bacterium Rhodobacter sphaeroides EBL0706 as a Strain of Luteovulum azotoformans.',
                                         '2021'],
                                        # ['', '', '', ''],
                                    ]
                                }
                            ]
                        },
                        {
                            'title': 'Taxonomy',
                            'expectations': [
                                {
                                    'type': 'text',
                                    'xpath': 'div[@data-element="new-lineage"]/div[1]',
                                    'data': 'New Lineage'
                                },
                                {
                                    'type': 'text',
                                    'xpath': 'div[@data-element="new-lineage"]/div[2]',
                                    'data': 'No lineage found'
                                }
                            ]
                        },
                        {
                            'title': 'Assembly and Annotation',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['RSP_4039', 'NC_007488', '1733', '+', '363', 'CDS',
                                         'IMG reference gene:2512957466; PFAM: Protein of unknown function, DUF583'],
                                        # ['', '', '', '', '', '', ''],
                                    ]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'name': 'overview',
                    'tabs': [
                        ['Type', 'Genome'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/5/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'data': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseGenomes'],
                                    ['Type', 'Genome'],
                                    ['Type Version', '7.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/5/1']
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
                                'data': [[
                                    'Rhodobacter_sphaeroides_2.4.1.contigset',
                                    'ContigSet',
                                    'Jan 15, 2015',
                                    'kbasetest'
                                ]]
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
