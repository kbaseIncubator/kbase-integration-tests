from tests.kbase_ui.plugins.PluginBase import PluginBase


class SearchTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('search')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Data Search (BETA)')
        self.wait_for_title('Data Search (BETA) | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('search')
