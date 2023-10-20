from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenome3Test(DataviewBase):
    def test_authenticated_prochlorococcus_2(self):
        object_case = {
            'ref': '45593/11/1',
            'name': 'prokka_ouput_1',
            'type': 'KBaseGenomes.Genome-17.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
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
                                                ['Name', 'Prochlorococcus marinus str. AS9601'],
                                                ['KBase Genome ID', 'GCF_000015645.1'],
                                                ['Domain', 'Bacteria'],
                                                ['DNA Length', '1,669,886'],
                                                ['Source', 'RefSeq'],
                                                ['Source ID', 'NC_008816'],
                                                ['Number of Contigs', '1'],
                                                ['GC Content', '31.32%'],
                                                ['Genetic Code', '11'],
                                                ['Number of Features', '1,780']
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
                                                'marine cyanobacteria with an unusual pigmentation'
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
                                            'type': 'text',
                                            'contains': [
                                                'Sorry, nothing found for '
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
                                            'type': 'text',
                                            'contains': [
                                                'Taxonomy provided by this Object and linked to NCBI.'
                                            ]
                                        },
                                        {
                                            'type': 'rotated_table',
                                            'data': [
                                                ['Scientific Name', 'Prochlorococcus marinus str. AS9601']
                                            ]
                                        }
                                    ]
                                },
                                {
                                    'title': 'Species Tree',
                                    'expectations': [
                                        {
                                            'type': 'text',
                                            'contains': [
                                                'A species tree was not found for this genome.'
                                            ]
                                        }
                                    ]
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
                                    'expectations': [
                                        # TODO: svg testing?
                                    ]
                                },
                                {
                                    'title': 'Gene Table',
                                    'expectations': [{
                                        'type': 'table',
                                        'data': [
                                            ['A9601_RS09110', 'NC_008816', '168', '+', '1158', 'gene',
                                             'DNA polymerase III subunit beta'],
                                        ]
                                    }]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'name': 'overview',
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'Genome'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/11/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseGenomes'],
                                    ['Type', 'Genome'],
                                    ['Type Version', '17.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/11/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
                                    ['Taxonomy',
                                     'cellular organisms; Bacteria; Terrabacteria group; Cyanobacteria/Melainabacteria group; Cyanobacteria; Synechococcales; Prochloraceae; Prochlorococcus; Prochlorococcus marinus'],
                                    ['Size', '1669886'],
                                    ['Source', 'RefSeq'],
                                    ['Name', 'Prochlorococcus marinus str. AS9601'],
                                    ['GC content', '0.313215393146598'],
                                    ['Genetic code', '11'],
                                    ['Type', 'Unknown'],
                                    ['Number of Genome Level Warnings', '2'],
                                    ['Source ID', 'NC_008816'],
                                    ['Number of Protein Encoding Genes', '1780'],
                                    ['Assembly Object', '15792/63937/1'],
                                    ['Number contigs', '1'],
                                    ['Domain', 'Bacteria'],
                                    ['Number of CDS', '1780'],
                                    ['MD5', 'fe2f8dd92cdb389c7921ae1b5394b143']
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
                                    [
                                        None,
                                        'seed_subsystem_ontology',
                                        'OntologyDictionary',
                                        'Apr 18, 2016',
                                        'jplfaria'
                                    ],
                                    [
                                        None,
                                        '146891_taxon',
                                        'Taxon',
                                        'Jan 6, 2017',
                                        'kbasetest'
                                    ],
                                    [
                                        None,
                                        'GCF_000015645.1_assembly',
                                        'Assembly',
                                        'Jan 30, 2017',
                                        'qzhang'
                                    ],
                                    [
                                        None,
                                        'prokka_ouput_1',
                                        'Genome',
                                        'Apr 3, 2020',
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
