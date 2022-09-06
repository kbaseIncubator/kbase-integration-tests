from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


#
# Other than the "data view" tab, this is the same as test_genome.py
#

class DataviewGenomeTest(DataviewBase):
    def test_authenticated_rhodobacter(self):
        object_case = {
            'ref': '45593/5/1',
            'sub': 'Feature',
            'subid': 'RSP_4039',
            'name': 'Rhodobacter_sphaeroides_2.4.1',
            'type': 'KBaseGenomes.Genome-7.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
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
                                         'IMG reference gene:2512957466; PFAM: Protein of unknown function, DUF583'],
                                        ['Subsystems', 'No subsystem data'],
                                        ['Annotation Comments', 'No annotation comments'],
                                        ['Genome', 'Rhodobacter sphaeroides 2.4.1'],
                                        ['Length', 'n/a, 120 aa'],
                                        ['Location', '1,733 to 2,095 (+)'],
                                        ['Aliases', 'REF_jgi:RSP_4039\nYP_345167.1'],
                                        ['CDSs', 'n/a']
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
                                        ['Protein length', '120 aa'],
                                        ['Protein translation',
                                         'MKTPNGQTASWPAPAAPDMRRSVVAPDLVVEGEMSSAGPVDVQGTVVGGV\nEAPEVVVAEAGRIEGSVTAHDLAVLGRISGSVSARQVRLGPSAVVQAHVL\nHERIAIEAGAELDGRLQRKA'],
                                        ['Feature Length', 'n/a'],
                                        ['Feature', 'n/a']
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
