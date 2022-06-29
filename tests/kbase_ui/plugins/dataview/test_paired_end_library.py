from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewPairdEndLibraryTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/4/1',
            'name': 'rhodobacter.art.q20.int.PE.reads',
            'type': 'KBaseFile.PairedEndLibrary-2.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'expectations': [
                        {
                            'type': 'table',
                            'data': [
                                ['Left reads source file name', '235066e6-35d8-49e5-a7da-b012934835a6.inter.fastq.gz'],
                                ['Sequencing technology', 'Illumina']
                            ]
                        }
                    ]
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'PairedEndLibrary'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/4/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseFile'],
                                    ['Type', 'PairedEndLibrary'],
                                    ['Type Version', '2.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/4/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
                                    ['sequencing_tech', 'Illumina'],
                                    ['single_genome', '1']
                                ]
                            }
                        },
                        {
                            'label': 'Versions',
                            'expected': {
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
                                'no_data_message': 'This object does not reference any other data object.'
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
