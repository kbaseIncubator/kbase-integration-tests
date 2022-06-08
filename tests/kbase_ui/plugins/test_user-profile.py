from tests.kbase_ui.plugins.PluginBase import PluginBase


class UserProfileTest(PluginBase):
    def test_authenticated_own_profile(self):
        self.login_navigate('people')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Your User Profile')
        self.wait_for_title('Your User Profile | KBase')

    def test_authenticated_other_profile(self):
        self.login_navigate('people/narrativetester')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'User Profile for Narrative Tester')
        self.wait_for_title('User Profile for Narrative Tester | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('people/narrativetester')
