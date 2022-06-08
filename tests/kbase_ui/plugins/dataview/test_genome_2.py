from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenome2Test(DataviewBase):
    def test_authenticated_prochlorococcus_1(self):
        object_case = {
            'ref': '45593/13/1',
            'name': 'prochloroccous_reannotated_with_prokka',
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
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/13/1']
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
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/13/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'data': [
                                    ['Taxonomy',
                                     'Bacteria; Terrabacteria group; Cyanobacteria/Melainabacteria group; Cyanobacteria; Synechococcales; Prochloraceae; Prochlorococcus; Prochlorococcus marinus'],
                                    ['Size', '1669886'],
                                    ['Source', 'RefSeq'],
                                    ['Name', 'Prochlorococcus marinus str. AS9601'],
                                    ['GC content', '0.31322'],
                                    ['Genetic code', '11'],
                                    ['Number of Genome Level Warnings', '0'],
                                    ['Source ID', 'NC_008816'],
                                    ['Number of Protein Encoding Genes', '1799'],
                                    ['Assembly Object', '15792/63937/3'],
                                    ['Number contigs', '1'],
                                    ['Domain', 'Bacteria'],
                                    ['Number of CDS', '1799'],
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
                                'data': [
                                    [
                                        'kb_prokka_report_5c28d202-3e52-416a-bf88-443e9825e56e',
                                        'Report',
                                        'Jun 6, 2022',
                                        'kbaseuitest'
                                    ]
                                ]
                            }
                        },
                        {
                            'label': 'References',
                            'expected': {
                                'data': [

                                    [
                                        'GCF_000015645.1_assembly',
                                        'Assembly',
                                        'Jan 29, 2020',
                                        'jayrbolton'
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
