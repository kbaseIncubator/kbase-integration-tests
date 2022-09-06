from tests.kbase_ui.plugins.dataview.DataviewBase import DataviewBase


class DataviewFBAModelTest(DataviewBase):
    def test_authenticated(self):
        object_case = {
            'ref': '45593/19/1',
            'name': 'test_imported_FBAModel',
            'type': 'KBaseFBA.FBAModel-14.0',
            'header': {
                'saved': 'Saved Jun 6, 2022 by kbaseuitest'
            },
            'tabs': {
                'dataview': {
                    'label': 'Data View',
                    'tabs': [
                        {
                            'label': 'Overview',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['Name', 'test_imported_FBAModel'],
                                        ['ID', 'kbaseuitest:narrative_1578347520053/test_imported_FBAModel'],
                                        ['Object type', 'KBaseFBA.FBAModel-14.0'],
                                        ['Owner', 'kbaseuitest'],
                                        ['Version', '1'],
                                    ]
                                }
                            ]
                        },
                        {
                            'label': 'Reactions',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['vad[undefined]', 'vad', 'GS[c0]\n<=>\nAMP[c0]', '∅', '∅'],
                                        ['vatpase[undefined]\n(rxn33888)', 'vatpase', 'ADP[c0]\n<=>\nATP[c0]', '∅',
                                         '∅'],
                                        ['vazglndem[undefined]', 'vazglndem', 'AZGLN[c0]\n<=>', '∅', '∅'],
                                        ['vazgludem[undefined]', 'vazgludem', 'AZGLU[c0]\n<=>', '∅', '∅'],
                                        ['vdead[undefined]', 'vdead', 'AMP[c0]\n<=>\nGS[c0]', '∅', '∅']
                                    ]
                                }
                            ]
                        },
                        {
                            'label': 'Compounds',
                            'expectations': [
                                {
                                    'type': 'table',
                                    'data': [
                                        ['ADP[undefined]\n(cpd00008)', 'ADP', '*', '1', 'c0'],
                                        ['AMP[undefined]\n(cpd00018)', 'AMP', '*', '1', 'c0'],
                                        ['ATP[undefined]\n(cpd00002)', 'ATP', '*', '1', 'c0'],
                                        ['AZGLN[undefined]', 'AZGLN', '*', '1', 'c0'],
                                        ['AZGLU[undefined]', 'AZGLU', '*', '1', 'c0'],
                                    ]
                                }
                            ]
                        }
                    ]
                },
                'overview': {
                    'label': 'Object Overview',
                    'rotated_table': [
                        ['Type', 'FBAModel'],
                        ['In Narrative', '`dataview` Test Cases'],
                        ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                        ['Permalink', 'https://ci.kbase.us/#dataview/45593/19/1']
                    ],
                    'panels': [
                        {
                            'label': 'Object Info',
                            'expected': {
                                'rotated_table': [
                                    ['Object Version', '1'],
                                    ['Type Module', 'KBaseFBA'],
                                    ['Type', 'FBAModel'],
                                    ['Type Version', '14.0'],
                                    ['In Narrative', '`dataview` Test Cases'],
                                    ['Last Updated', 'Jun 6, 2022 by kbaseuitest'],
                                    ['Permalink', 'https://ci.kbase.us/#dataview/45593/19/1']
                                ]
                            }
                        },
                        {
                            'label': 'Metadata',
                            'expected': {
                                'rotated_table': [
                                    ['Number gapgens', '0'],
                                    ['Type', 'SBML Model'],
                                    ['Number gapfills', '0'],
                                    ['Source ID', 'test_imported_FBAModel'],
                                    ['Number biomasses', '0'],
                                    ['Number compartments', '1'],
                                    ['Genome', '1067/1/1'],
                                    ['Source', 'External'],
                                    ['Number compounds', '12'],
                                    ['Number reactions', '16'],
                                    ['Name', 'test_imported_FBAModel'],
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
                                        'fliu_test_report_9f6c322f-3421-4849-8cdd-70a96f176739',
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
                                        'Empty',
                                        'Genome',
                                        'Aug 4, 2015',
                                        'seaver'
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
