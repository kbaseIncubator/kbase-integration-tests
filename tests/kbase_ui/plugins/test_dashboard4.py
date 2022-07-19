from tests.kbase_ui.plugins.PluginBase import PluginBase


class Dashboard4Test(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('dashboard4')

        # Make sure the default title appears
        self.assert_title('Dashboard the Fourth')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('dashboard4')
