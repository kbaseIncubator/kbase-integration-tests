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
                    'expectations': []
                },
                'overview': {
                    'name': 'overview',
                    'tabs': [
                        ['Type', 'Genome'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/11/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'data': [
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
                                'data': [
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
                                'data': [
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
                                'data': [
                                    [
                                        '146891_taxon',
                                        'Taxon',
                                        'Jan 6, 2017',
                                        'kbasetest'
                                    ],
                                    [
                                        'GCF_000015645.1_assembly',
                                        'Assembly',
                                        'Jan 30, 2017',
                                        'qzhang'
                                    ],
                                    [
                                        'seed_subsystem_ontology',
                                        'OntologyDictionary',
                                        'Apr 18, 2016',
                                        'jplfaria'
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
