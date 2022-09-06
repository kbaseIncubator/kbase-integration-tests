from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenome3Test(DataviewBase):
    def test_authenticated_prochlorococcus_2(self):
        object_case = {
            'ref': '45593/11/1',
            'sub': 'Feature',
            'subid': 'A9601_RS09110',
            'name': 'prokka_ouput_1',
            'type': 'KBaseGenomes.Genome-17.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'sections': [
                        {
                            'title': 'Feature Overview',
                            'expectations': [
                                {
                                    'type': 'rotated_table',
                                    'data': [
                                        ['Functions',
                                         'DNA polymerase III subunit beta'],
                                        ['Subsystems', 'No subsystem data'],
                                        ['Annotation Comments', 'No annotation comments'],
                                        ['Genome', 'Prochlorococcus marinus str. AS9601'],
                                        ['Length', '1,158 bp, 385 aa'],
                                        ['Location', '168 to 1,325 (+)'],
                                        ['Aliases', [{
                                            'type': 'table',
                                            'data': [
                                                ['gene_synonym', 'A9601_RS09110'],
                                                ['gene_synonym', 'A9601_00001'],
                                                ['gene_synonym', 'GI:500141475'],
                                                ['gene_synonym', 'WP_011817478.1']
                                            ]
                                        }]],
                                        ['CDSs', 'WP_011817478.1']
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
                                        ['Protein translation',
                                         'MEIICNQNELNNAIQLVSKAVASRPTHPILANILLTADEGTNKISVTGFD\nLNLGIQTSFDGTVKNSGAITIPSKLLSEIVNKLPNETPVSLEVDENSDNI\nLIKSDRGSFNLKGIPSDEYPNLPFVESGTSLNIEPSSFLKALKSTIFASS\nNDDSKQLLTGVNFTFKPNYLESASTDGHRLAVALIGKEEQIENKENLSSN\nVDDLSVTIPTRSLREIEKLVSLRSSENSIKLFYDKGQVVFISSNQIITTR\nTLEGTYPNYSQLIPDSFSKIINFNTKKLIDSLERIAVLADQQSSVVKIKL\nDDTDLASISADAQDIGNANESIPVSYSGENFDIAFNVRYLLEGLKVIASE\nNVLLKCNIATTPAVFVPEDNLNSFTYLVMPVQVRS'],
                                        ['Feature Length', '1,158 bp'],
                                        ['Feature',
                                         'ATGGAAATTATTTGTAATCAAAATGAATTAAATAATGCTATACAACTAGT\nAAGCAAGGCAGTTGCTTCAAGGCCAACGCATCCAATTCTTGCAAACATAC\nTTTTAACAGCTGACGAAGGAACTAATAAAATTAGTGTCACAGGATTTGAC\nTTAAATTTAGGAATTCAAACTTCTTTTGATGGAACTGTCAAAAATAGTGG\nAGCTATCACTATACCCTCAAAACTTTTATCAGAAATAGTAAACAAACTAC\nCTAATGAAACTCCTGTTTCTCTAGAAGTAGACGAAAATTCAGATAATATT\nCTAATAAAAAGTGATAGAGGTTCTTTTAATCTAAAAGGGATACCCTCTGA\nTGAATATCCTAATTTGCCATTTGTTGAAAGCGGTACTTCTTTGAATATTG\nAGCCTAGTTCTTTTTTAAAGGCTTTAAAATCTACCATTTTTGCCAGTAGT\nAATGATGATTCAAAGCAACTACTCACAGGTGTCAATTTTACTTTCAAACC\nAAATTATTTAGAGTCTGCTTCTACAGATGGCCATAGATTGGCTGTTGCCT\nTAATTGGTAAGGAAGAACAAATTGAAAATAAAGAAAACTTATCTTCAAAT\nGTTGATGATTTATCGGTAACTATCCCAACTAGATCATTAAGAGAAATTGA\nAAAACTAGTATCTTTGAGAAGCTCAGAAAATTCAATTAAGCTTTTCTATG\nACAAAGGTCAAGTAGTATTTATATCTTCTAATCAAATAATTACTACGAGA\nACTTTAGAAGGTACTTATCCTAATTATTCACAATTAATTCCTGATTCTTT\nTTCTAAAATTATAAATTTTAATACAAAAAAATTAATTGATTCATTAGAAA\nGAATTGCTGTTTTGGCAGATCAGCAAAGTAGTGTTGTAAAGATTAAATTA\nGATGATACAGATTTAGCTTCAATCAGCGCAGATGCTCAAGATATTGGAAA\nTGCAAATGAATCAATACCTGTTTCTTATTCAGGAGAAAATTTTGATATTG\nCATTTAATGTAAGATATTTGTTAGAAGGTTTAAAAGTTATTGCCTCTGAA\nAATGTACTTTTAAAGTGTAATATTGCAACTACTCCAGCTGTTTTTGTACC\nAGAAGATAATCTCAATTCTTTTACGTATCTAGTTATGCCAGTGCAGGTTC\nGTTCTTAA']
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
