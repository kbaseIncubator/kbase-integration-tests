from tests.kbase_ui.plugins.PluginBase import PluginBase


class AuthTest(PluginBase):
    def test_unauthenticated_login_page(self):
        self.navigate('login')

        # Make sure the default title appears
        self.wait_for_title('KBase: KBase Sign In')

        self.switch_to_kbase_ui_iframe()

        # plugin_xpath = '//*[@data-plugin="auth2-client"]'

        # TODO: plugin testhook is nested inside the plugin!
        self.find_by_text('Welcome to KBase')

        self.wait_for_elements_by_xpath('//*[@role="button" and @title="Sign In button for the Globus identity provider"]')
        self.wait_for_elements_by_xpath('//*[@role="button" and @title="Sign In button for the Google identity provider"]')
        self.wait_for_elements_by_xpath('//*[@role="button" and @title="Sign In button for the ORCID identity provider"]')
        
        # There is also an icon in the button, so we need to use an inexact text comparison.
        self.wait_for_elements_by_xpath('//*[@role="button" and contains(., "Need Help?")]')
 
