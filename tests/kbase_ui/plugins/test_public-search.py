from tests.kbase_ui.plugins.PluginBase import PluginBase


class PublicSearchTest(PluginBase):
    def test_authenticated_search(self):
        self.login_navigate('public-search')

        # Make sure the default title appears
        self.assert_title('KBase Data Search')

    def test_unauthenticated_search(self):
        self.navigate('public-search')

        # Make sure the default title appears
        self.assert_title('KBase Data Search')
