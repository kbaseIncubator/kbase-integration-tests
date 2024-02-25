from tests.kbase_ui.plugins.PluginBase import PluginBase


class OrganizationsTest(PluginBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('orgs')

        # Make sure the default title appears
        self.wait_for_title('KBase: Organizations')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('orgs', 'KBase Organizations')
