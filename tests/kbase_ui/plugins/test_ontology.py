from tests.kbase_ui.plugins.PluginBase import PluginBase


class OntologyTest(PluginBase):
    def test_authenticated_ontology_term(self):
        namespace = 'envo_ontology'
        term = 'ENVO:00001998'
        name = 'soil'
        path = f'ontology/term/{namespace}/{term}'
        self.login_navigate(path)

        title = f'KBase: Ontology Landing Page for "{name}" ({term})'
        self.wait_for_title(title)

    def test_unauthenticated_ontology_term(self):
        namespace = 'envo_ontology'
        term = 'ENVO:00001998'
        path = f'ontology/term/{namespace}/{term}'
        self.auth_blocked_plugin(path, 'Ontology Viewer')
