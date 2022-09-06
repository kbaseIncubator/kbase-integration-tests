from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenome2Test(DataviewBase):
    def test_authenticated_prochlorococcus_1(self):
        object_case = {
            'ref': '45593/13/1',
            'sub': 'cds',
            'subid': 'A9601_RS09110_CDS_1',
            'name': 'prochloroccous_reannotated_with_prokka',
            'type': 'KBaseGenomes.Genome-17.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'sections': [
                        {
                            'title': 'CDS Overview',
                            'expectations': [
                                {
                                    'type': 'rotated_table',
                                    'data': [
                                        ['Genome', 'GCF_000015645.1'],
                                        ['Scientific name', 'Prochlorococcus marinus str. AS9601'],
                                        ['Functions', 'DNA polymerase III subunit beta'],
                                        ['Length', '1,158 bp, 385 aa'],
                                        ['Location', '168 to 1,325 (+)'],
                                        ['Aliases', [{
                                            'type': 'table',
                                            'data': [
                                                ['locus_tag', 'A9601_RS09110'],
                                                ['old_locus_tag', 'A9601_00001'],
                                                ['EC_number', '2.7.7.7'],
                                                ['protein_id', 'WP_011817478.1']
                                            ]
                                        }]],
                                        ['Note',
                                         'Derived by automated computational analysis using gene prediction method: Protein Homology.'],
                                        ['Warnings', 'n/a']
                                    ]
                                }
                            ]
                        },
                        {
                            'title': 'Sequence',
                            'expectations': [
                                {
                                    'type': 'rotated_table',
                                    'data': [
                                        ['Protein length', '385 aa'],
                                        ['Protein translation', [{
                                            'type': 'lines',
                                            'data': [
                                                'MEIICNQNELNNAIQLVSKAVASRPTHPILANILLTADEGTNKISVTGFD',
                                                'LNLGIQTSFDGTVKNSGAITIPSKLLSEIVNKLPNETPVSLEVDENSDNI',
                                                'LIKSDRGSFNLKGIPSDEYPNLPFVESGTSLNIEPSSFLKALKSTIFASS',
                                                'NDDSKQLLTGVNFTFKPNYLESASTDGHRLAVALIGKEEQIENKENLSSN',
                                                'VDDLSVTIPTRSLREIEKLVSLRSSENSIKLFYDKGQVVFISSNQIITTR',
                                                'TLEGTYPNYSQLIPDSFSKIINFNTKKLIDSLERIAVLADQQSSVVKIKL',
                                                'DDTDLASISADAQDIGNANESIPVSYSGENFDIAFNVRYLLEGLKVIASE',
                                                'NVLLKCNIATTPAVFVPEDNLNSFTYLVMPVQVRS'
                                            ]
                                        }]],
                                        ['CDS Length', '1,158 bp'],
                                        ['CDS', [{
                                            'type': 'lines',
                                            'data': [
                                                'ATGGAAATTATTTGTAATCAAAATGAATTAAATAATGCTATACAACTAGT',
                                                'AAGCAAGGCAGTTGCTTCAAGGCCAACGCATCCAATTCTTGCAAACATAC',
                                                'TTTTAACAGCTGACGAAGGAACTAATAAAATTAGTGTCACAGGATTTGAC',
                                                'TTAAATTTAGGAATTCAAACTTCTTTTGATGGAACTGTCAAAAATAGTGG',
                                                'AGCTATCACTATACCCTCAAAACTTTTATCAGAAATAGTAAACAAACTAC',
                                                'CTAATGAAACTCCTGTTTCTCTAGAAGTAGACGAAAATTCAGATAATATT',
                                                'CTAATAAAAAGTGATAGAGGTTCTTTTAATCTAAAAGGGATACCCTCTGA',
                                                'TGAATATCCTAATTTGCCATTTGTTGAAAGCGGTACTTCTTTGAATATTG',
                                                'AGCCTAGTTCTTTTTTAAAGGCTTTAAAATCTACCATTTTTGCCAGTAGT',
                                                'AATGATGATTCAAAGCAACTACTCACAGGTGTCAATTTTACTTTCAAACC',
                                                'AAATTATTTAGAGTCTGCTTCTACAGATGGCCATAGATTGGCTGTTGCCT',
                                                'TAATTGGTAAGGAAGAACAAATTGAAAATAAAGAAAACTTATCTTCAAAT',
                                                'GTTGATGATTTATCGGTAACTATCCCAACTAGATCATTAAGAGAAATTGA',
                                                'AAAACTAGTATCTTTGAGAAGCTCAGAAAATTCAATTAAGCTTTTCTATG',
                                                'ACAAAGGTCAAGTAGTATTTATATCTTCTAATCAAATAATTACTACGAGA',
                                                'ACTTTAGAAGGTACTTATCCTAATTATTCACAATTAATTCCTGATTCTTT',
                                                'TTCTAAAATTATAAATTTTAATACAAAAAAATTAATTGATTCATTAGAAA',
                                                'GAATTGCTGTTTTGGCAGATCAGCAAAGTAGTGTTGTAAAGATTAAATTA',
                                                'GATGATACAGATTTAGCTTCAATCAGCGCAGATGCTCAAGATATTGGAAA',
                                                'TGCAAATGAATCAATACCTGTTTCTTATTCAGGAGAAAATTTTGATATTG',
                                                'CATTTAATGTAAGATATTTGTTAGAAGGTTTAAAAGTTATTGCCTCTGAA',
                                                'AATGTACTTTTAAAGTGTAATATTGCAACTACTCCAGCTGTTTTTGTACC',
                                                'AGAAGATAATCTCAATTCTTTTACGTATCTAGTTATGCCAGTGCAGGTTC',
                                                'GTTCTTAA'
                                            ]
                                        }]]
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
                        ['Type', 'Genome'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/13/1']
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
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/13/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
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
                                'table': [
                                    ['v1', 'Saved on Jun 6, 2022 by kbaseuitest']
                                ]
                            }
                        },
                        {
                            'label': 'Referenced by',
                            'expected': {
                                'data_table': [
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
                                'data_table': [
                                    [
                                        None,
                                        'GCF_000015645.1_assembly',
                                        'Assembly',
                                        'Jan 29, 2020',
                                        'jayrbolton'
                                    ],
                                    [
                                        None,
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
