from tests.kbase_ui.plugins.PluginBase import PluginBase


class Dashboard4Test(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('dashboard4')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Dashboard the Fourth')
        self.wait_for_title('Dashboard the Fourth | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('dashboard4')
