from tests.kbase_ui.plugins.PluginBase import PluginBase


class JobsBrowserTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('jobbrowser')

        # Make sure the default title appears
        self.assert_title('Job Browser')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('jobbrowser')
