from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewGenome2Test(DataviewBase):
    def test_authenticated_prochlorococcus_1(self):
        object_case = {
            'ref': '45593/13/1',
            'sub': 'Feature',
            'subid': 'A9601_RS09110',
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
                            'title': 'Feature Overview',
                            'expectations': [
                                {
                                    'type': 'rotated_table',
                                    'data': [
                                        ['Functions',
                                         'Beta sliding clamp'],
                                        ['Subsystems', 'No subsystem data'],
                                        ['Annotation Comments', 'No annotation comments'],
                                        ['Genome', 'Prochlorococcus marinus str. AS9601'],
                                        ['Length', '1,158 bp, 385 aa'],
                                        ['Location', '168 to 1,325 (+)'],
                                        # Note that the table layout is transformed into tabs and newlines
                                        # TODO: use table expectation
                                        ['Aliases',
                                         'protein_id\tWP_011817478.1\nEC_number\t2.7.7.7\nold_locus_tag\tA9601_00001\nlocus_tag\tA9601_RS09110'],
                                        ['CDSs', 'A9601_RS09110_CDS_1']
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
                                         'ATGGAAATTATTTGTAATCAAAATGAATTAAATAATGCTATACAACTAGT\nAAGCAAGGCAGTTGCTTCAAGGCCAACGCATCCAATTCTTGCAAACATAC\nTTTTAACAGCTGACGAAGGAACTAATAAAATTAGTGTCACAGGATTTGAC\nTTAAATTTAGGAATTCAAACTTCTTTTGATGGAACTGTCAAAAATAGTGG\nAGCTATCACTATACCCTCAAAACTTTTATCAGAAATAGTAAACAAACTAC\nCTAATGAAACTCCTGTTTCTCTAGAAGTAGACGAAAATTCAGATAATATT\nCTAATAAAAAGTGATAGAGGTTCTTTTAATCTAAAAGGGATACCCTCTGA\nTGAATATCCTAATTTGCCATTTGTTGAAAGCGGTACTTCTTTGAATATTG\nAGCCTAGTTCTTTTTTAAAGGCTTTAAAATCTACCATTTTTGCCAGTAGT\nAATGATGATTCAAAGCAACTACTCACAGGTGTCAATTTTACTTTCAAACC\nAAATTATTTAGAGTCTGCTTCTACAGATGGCCATAGATTGGCTGTTGCCT\nTAATTGGTAAGGAAGAACAAATTGAAAATAAAGAAAACTTATCTTCAAAT\nGTTGATGATTTATCGGTAACTATCCCAACTAGATCATTAAGAGAAATTGA\nAAAACTAGTATCTTTGAGAAGCTCAGAAAATTCAATTAAGCTTTTCTATG\nACAAAGGTCAAGTAGTATTTATATCTTCTAATCAAATAATTACTACGAGA\nACTTTAGAAGGTACTTATCCTAATTATTCACAATTAATTCCTGATTCTTT\nTTCTAAAATTATAAATTTTAATACAAAAAAATTAATTGATTCATTAGAAA\nGAATTGCTGTTTTGGCAGATCAGCAAAGTAGTGTTGTAAAGATTAAATTA\nGATGATACAGATTTAGCTTCAATCAGCGCAGATGCTCAAGATATTGGAAA\nTGCAAATGAATCAATACCTGTTTCTTATTCAGGAGAAAATTTTGATATTG\nCATTTAATGTAAGATATTTGTTAGAAGGTTTAAAAGTTATTGCCTCTGAA\nAATGTACTTTTAAAGTGTAATATTGCAACTACTCCAGCTGTTTTTGTACC\nAGAAGATAATCTCAATTCTTTTACGTATCTAGTTATGCCAGTGCAGGTTC\nGTTCTTAA']]
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
