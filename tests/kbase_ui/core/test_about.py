from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class AboutTest(KBaseUIBase):
    def test_authenticated_initial_page(self):
        self.login_navigate('')

        # self.wait_for_titles('Narratives Navigator')
        # This currently ends up on the Navigator, which does not use
        # the same layout as kbase-ui, so let's roll by hand.
        expected_title = 'Narratives Navigator'
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//h1'), expected_title))

    def test_unauthenticated_initial_page(self):
        self.navigate('')

        # Make sure the default unauthenticated title appears
        self.wait_for_titles('KBase Sign In')

        self.switch_to_iframe()

        # These look for some element which includes the given text
        self.find_element_with_text('Welcome to KBase')
        self.find_element_with_text('New to KBase?')
        self.find_element_with_text('Need Help?')

    # About Page

    def assert_about(self):
        self.wait_for_titles('About')
        self.wait_for_text('component', 'mainwindow', 'About')
        # self.wait_for_text('panel', 'welcome', 'The KBase User Interface')
        self.wait_for_panel_title('welcome', 'The KBase User Interface')
        self.wait_for_panel_title('build-info', 'This Version')

    def test_unauthenticated_about(self):
        self.navigate('about')
        self.assert_about()

    def test_authenticated_about(self):
        self.login_navigate('about')
        self.assert_about()

    # About Services Page

    def test_unauthenticated_about_services(self):
        self.navigate('about/services')

        self.wait_for_titles('KBase Core and Dynamic Service Versions and Perf')

    # About Plugins Page

    def test_unauthenticated_about_plugins(self):
        self.navigate('about/plugins')

        self.wait_for_titles('About KBase UI Plugins')
