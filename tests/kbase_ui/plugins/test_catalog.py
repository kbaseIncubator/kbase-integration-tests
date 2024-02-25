from tests.kbase_ui.plugins.PluginBase import PluginBase


class CatalogTest(PluginBase):
    def test_authenticated_catalog_apps(self):
        self.login_navigate('catalog/apps')

        # Make sure the title appears
        self.wait_for_title('KBase: App Catalog')

    def test_unauthenticated_catalog_apps(self):
        self.navigate('catalog/apps')

        # Make sure the title appears
        self.wait_for_title('KBase: App Catalog')
