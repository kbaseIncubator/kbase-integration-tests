from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewSingleEndLibraryTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/3/1',
            'name': 'rhodobacter.art.q50.SE.reads',
            'type': 'KBaseFile.SingleEndLibrary-2.0',
            'header': {
                'saved': 'Saved Jun 3, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'not_supported': True
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'SingleEndLibrary'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/3/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseFile'],
                                    ['Type', 'SingleEndLibrary'],
                                    ['Type Version', '2.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 3, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/3/1']
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
                                'data_table': [
                                    [
                                        None, 'rhodo.art.q50.SE.reads', 'SingleEndLibrary', 'Oct 5, 2016',
                                        'pranjan77'
                                    ],
                                    [
                                        None, 'rhodobacter.art.q50.SE.reads', 'SingleEndLibrary',
                                        'Oct 5, 2016', 'kbasetest'
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
