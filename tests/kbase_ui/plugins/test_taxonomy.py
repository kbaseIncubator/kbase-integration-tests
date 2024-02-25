from tests.kbase_ui.plugins.PluginBase import PluginBase


class TaxonomyTest(PluginBase):
    def test_authenticated_taxonomy_view(self):
        # https://ci.kbase.us/#taxonomy/taxon/ncbi_taxonomy/562
        namespace = 'ncbi_taxonomy'
        taxon_id = '562'
        name = 'Escherichia coli'
        path = f'taxonomy/taxon/{namespace}/{taxon_id}'
        self.login_navigate(path)

        title = f'KBase: Taxonomy Landing Page for "{name}"'
        self.wait_for_title(title)

    def test_unauthenticated_taxonomy_view(self):
        # https://ci.kbase.us/#taxonomy/taxon/ncbi_taxonomy/562
        namespace = 'ncbi_taxonomy'
        id = '562'
        path = f'taxonomy/taxon/{namespace}/{id}'
        self.auth_blocked_plugin(path, 'Taxonomy Viewer')
