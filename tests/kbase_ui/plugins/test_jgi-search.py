from tests.kbase_ui.plugins.PluginBase import PluginBase


class JGISearchTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('jgi-search')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'JGI Search (BETA)')
        self.wait_for_title('JGI Search (BETA) | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('jgi-search')
