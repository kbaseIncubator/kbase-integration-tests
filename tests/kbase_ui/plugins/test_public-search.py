from tests.kbase_ui.plugins.PluginBase import PluginBase


class PublicSearchTest(PluginBase):
    def test_authenticated_search(self):
        self.login_navigate('public-search')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'KBase Data Search')
        self.wait_for_title('KBase Data Search | KBase')

    def test_unauthenticated_search(self):
        self.navigate('public-search')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'KBase Data Search')
        self.wait_for_title('KBase Data Search | KBase')
