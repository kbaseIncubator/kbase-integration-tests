from tests.kbase_ui.plugins.PluginBase import PluginBase


class JobsBrowserTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('jobbrowser')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Job Browser')
        self.wait_for_title('Job Browser | KBase')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('jobbrowser')
