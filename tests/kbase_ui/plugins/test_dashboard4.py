from tests.kbase_ui.plugins.PluginBase import PluginBase


class Dashboard4Test(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('dashboard4')
        self.wait_for_title('KBase: Dashboard the Fourth')
        self.wait_for_header_title('Dashboard the Fourth')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('dashboard4', 'Yet Another Dashboard')
