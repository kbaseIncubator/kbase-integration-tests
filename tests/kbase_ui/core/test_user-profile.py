from tests.kbase_ui.plugins.PluginBase import PluginBase


class UserProfileTest(PluginBase):
    def test_authenticated_own_profile(self):
        self.login_navigate('people')

        # Make sure the default title appears
        self.assert_title('Your User Profile')

    def test_authenticated_other_profile(self):
        self.login_navigate('people/narrativetester')

        # Make sure the default title appears
        self.assert_title('User Profile for Narrative Tester')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('people/kbaseuitest', 'User Profile')
