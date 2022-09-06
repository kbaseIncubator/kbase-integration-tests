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
                    'label': 'Data View',
                    'tabs': [
                        {
                            'label': 'Genome Overview',
                            'sections': [
                                {
                                    'title': 'Summary and Stats',
                                    'expectations': [
                                        {
                                            'type': 'rotated_table',
                                            'data': [
                                                ['Name', 'Rhodobacter sphaeroides 2.4.1'],
                                                ['KBase Genome ID', 'Rhodobacter_sphaeroides_2.4.1'],
                                                ['Domain', 'Bacteria'],
                                                ['DNA Length', '4,602,977'],
                                                ['Source', 'NCBI'],
                                                ['Source ID', 'NCBI'],
                                                ['Number of Contigs', '7'],
                                                ['GC Content', '68.79%'],
                                                ['Genetic Code', '11'],
                                                ['Number of Features', '4,347']
                                            ]
                                        }
                                    ]
                                },
                                {
                                    'title': 'From Wikipedia',
                                    'expectations': [
                                        {
                                            'type': 'text',
                                            'contains': [
                                                'is a kind of purple bacterium',
                                                'The regulation of its photosynthetic machinery is of great interest'
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'label': 'Publications',
                            'sections': [
                                {
                                    'title': 'Publications in PubMed',
                                    'expectations': [
                                        {
                                            'type': 'data-table',
                                            'data': [
                                                ['Environmental research',
                                                 'Jawaharraj K, Sigdel P, Gu Z, Muthusamy G, Sani R, Gadhamshetty V',
                                                 'Photosynthetic microbial fuel cells for methanol treatment using graphene electrodes.',
                                                 '2022'],

                                                ['Microorganisms',
                                                 'Wang H, Sha X, Li R, Li Y, Khaleque HN, Zhang Y, Bohu T, Bai Z, Zhuang X',
                                                 'Comparative Genome Analysis Provides Molecular Evidence for Reclassification of the Photosynthetic Bacterium Rhodobacter sphaeroides EBL0706 as a Strain of Luteovulum azotoformans.']
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'label': 'Taxonomy',
                            'sections': [
                                {
                                    'title': 'Lineage',
                                    'expectations': [
                                        {
                                            'type': 'rotated_table',
                                            'data': [
                                                ['Scientific Name', 'Rhodobacter sphaeroides 2.4.1']
                                            ]
                                        }
                                    ]
                                },
                                {
                                    'title': 'Species Tree',
                                    'expectations': [{
                                        'type': 'text',
                                        'contains': [
                                            'A species tree was not found for this genome.'
                                        ]
                                    }]
                                }
                            ]
                        }, {
                            'label': 'Assembly and Annotation',
                            'sections': [
                                {
                                    'title': 'Contig Browser',
                                    'expectations': [{
                                        'type': 'text',
                                        'contains': [
                                            'Click on a feature to view details'
                                        ]
                                    }]
                                },
                                {
                                    'title': 'SEED Functions',
                                    'expectations': [{
                                        'type': 'text',
                                        'contains': [
                                            'No Functional Categories assigned, you can add them using the Narrative.'
                                        ]
                                    }]
                                },
                                {
                                    'title': 'Gene Table',
                                    'expectations': [{
                                        'type': 'table',
                                        'data': [
                                            ['RSP_4039', 'NC_007488', '1733', '+', '363', 'CDS',
                                             'IMG reference gene:2512957466; PFAM: Protein of unknown function, DUF583'],
                                        ]
                                    }]
                                }
                            ]
                        }]
                },
                'overview': {
                    'name': 'overview',
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'Genome'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/5/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
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
                                # Probably should be a rotated table, because it doesn't have
                                # a header row
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
                                'data_table': [[
                                    None,
                                    'Rhodobacter_sphaeroides_2.4.1.contigset',
                                    'ContigSet',
                                    'Jan 15, 2015',
                                    'kbasetest'
                                ], [
                                    None,
                                    'Rhodobacter_sphaeroides_2.4.1',
                                    'Genome',
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
