from tests.kbase_ui.plugins.PluginBase import PluginBase


class TypeviewTest(PluginBase):
    def test_authenticated_type_view(self):
        self.login_navigate('spec/type/KBaseBiochem.Media-4.2')

        # Make sure the default title appears
        self.assert_title('Type Specification for KBaseBiochem.Media-4.2', include_descendent=True)

    # https://ci.kbase.us/#spec/module/KBaseBiochem

    def test_authenticated_module_view(self):
        self.login_navigate('spec/module/KBaseBiochem')

        # Make sure the default title appears
        self.assert_title('Module Specification for KBaseBiochem', include_descendent=True)

    def test_unauthenticated_module_view(self):
        self.navigate('spec/module/KBaseBiochem')

        # Make sure the default title appears
        self.assert_title('Module Specification for KBaseBiochem', include_descendent=True)
