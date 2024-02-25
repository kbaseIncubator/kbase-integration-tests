from tests.kbase_ui.plugins.PluginBase import PluginBase


class JobsBrowserTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('jobbrowser')
        self.wait_for_title('KBase: Job Browser')
        self.wait_for_header_title('Job Browser')


    def test_unauthenticated(self):
        self.auth_blocked_plugin('jobbrowser', 'Job Browser')
