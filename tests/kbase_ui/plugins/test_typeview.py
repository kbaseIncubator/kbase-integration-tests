from tests.kbase_ui.plugins.PluginBase import PluginBase


class TypeviewTest(PluginBase):
    def test_authenticated_type_view(self):
        self.login_navigate('spec/type/KBaseBiochem.Media-4.2')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Type Specification for KBaseBiochem.Media-4.2')
        self.wait_for_title('Type Specification for KBaseBiochem.Media-4.2 | KBase')

    # https://ci.kbase.us/#spec/module/KBaseBiochem

    def test_authenticated_module_view(self):
        self.login_navigate('spec/module/KBaseBiochem')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Module Specification for KBaseBiochem')
        self.wait_for_title('Module Specification for KBaseBiochem | KBase')

    def test_unauthenticated_module_view(self):
        self.navigate('spec/module/KBaseBiochem')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Module Specification for KBaseBiochem')
        self.wait_for_title('Module Specification for KBaseBiochem | KBase')
