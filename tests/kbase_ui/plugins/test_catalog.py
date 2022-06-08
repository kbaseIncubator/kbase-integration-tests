from tests.kbase_ui.plugins.PluginBase import PluginBase


class CatalogTest(PluginBase):
    def test_authenticated_catalog_apps(self):
        self.login_navigate('catalog/apps')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'App Catalog')
        self.wait_for_title('App Catalog | KBase')

    def test_unauthenticated_catalog_apps(self):
        self.navigate('catalog/apps')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'App Catalog')
        self.wait_for_title('App Catalog | KBase')
