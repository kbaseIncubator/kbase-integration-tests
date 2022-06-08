from tests.kbase_ui.plugins.PluginBase import PluginBase


class AccountTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('auth2/account')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Account Manager')
        self.wait_for_title('Account Manager | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('auth2/account')
