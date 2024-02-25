from tests.kbase_ui.plugins.PluginBase import PluginBase


class BiochemSearchTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('biochem-search')

        # Make sure the default title appears
        self.assert_title('Biochem Search')

        self.switch_to_kbase_ui_plugin_iframe()

        # Make sure tabs are available
        self.wait_for_text('tab', 'Compounds', 'Compounds')
        self.wait_for_text('tab', 'Reactions', 'Reactions')

        # Ensure initial results "no data" messages are available.

        no_data_xpath = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['component', 'biochemistry-table'],
            ['element', 'render-no-data']
        ])
        self.wait_for_text_xpath(no_data_xpath, 'Please search for Compounds above')

        reactions_tab = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['tab', 'Reactions']
        ])
        self.click(reactions_tab)

        no_data_xpath = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['component', 'biochemistry-table'],
            ['element', 'render-no-data']
        ])
        self.wait_for_text_xpath(no_data_xpath, 'Please search for Reactions above')

    def test_authenticated_search(self):
        self.login_navigate('biochem-search')
        self.switch_to_kbase_ui_plugin_iframe()

        # search for "water"
        table_xpath = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['component', 'biochemistry-table']
        ])
        input_xpath = f'{table_xpath}//input'
        self.enter_text(input_xpath, 'water')
        self.push_enter(input_xpath)

        # look for expected results
        table = f"{self.kbase_testhook([['plugin', 'biochem-search'], ['component', 'biochemistry-table']])}//table/tbody"

        self.wait_for_table(table, [
            ['(+)', 'cpd00001', None, 'H2O', 'H2O', '18.0', '0',
             'Name: H20 H2O H3O+ HO- Hydroxide ion OH OH- Water hydrogen oxide hydroxide hydroxide ion hydroxyl hydroxyl ion oxonium water, AraCyc: OH WATER, BiGG: h2o oh1, BrachyCyc: WATER, KEGG: C00001 C01328, MetaCyc: OH OXONIUM WATER']
        ])

        # Now do it on the reactions tab
        reactions_tab = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['tab', 'Reactions']
        ])
        self.click(reactions_tab)

        # search for "water"
        table_xpath = self.kbase_testhook([
            ['plugin', 'biochem-search'],
            ['component', 'biochemistry-table']
        ])
        input_xpath = f'{table_xpath}//input'
        self.enter_text(input_xpath, 'water')
        self.push_enter(input_xpath)

        # look for expected results
        table = f"{self.kbase_testhook([['plugin', 'biochem-search'], ['component', 'biochemistry-table']])}//table/tbody"

        self.wait_for_table(table, [
            ['(+)', 'rxn00144', '2,3-diaminopropanoate ammonia-lyase (adding water; pyruvate-forming)',
             '(1) cpd00001[0] + (1) cpd00067[0] + (1) cpd03828[0] => (2) cpd00013[0] + (1) cpd00020[0]', '0.61', 'OK',
             'BiGG: DAPAL, KEGG: R00195, iAF1260: DAPAL, Name: 2,3-Diaminopropionate ammonia-lyase 2,3-diaminopropanoate ammonia-lyase (adding water pyruvate-forming) 2,3-diaminopropionate amonnia lyase']
        ])
