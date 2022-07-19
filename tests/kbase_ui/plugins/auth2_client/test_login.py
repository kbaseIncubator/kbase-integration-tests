from tests.kbase_ui.plugins.PluginBase import PluginBase


class AuthTest(PluginBase):
    def test_unauthenticated_login_page(self):
        self.navigate('login')

        # Make sure the default title appears
        self.assert_title('KBase Sign In')

        self.switch_to_iframe()

        plugin_xpath = '//*[@data-plugin="auth2-client"]'

        # TODO: plugin testhook is nested inside the plugin!
        self.find_by_text('Welcome to KBase')

        # Cannot test for button content since they are images, but we can test
        # for the button aria-label.
        self.assert_aria_button('Sign In button for the Google identity provider')
        self.assert_aria_button('Sign In button for the ORCID identity provider')
        self.assert_aria_button('Sign In button for the Globus identity provider')

        self.find_element_with_text('Sign Up', xpath='//button', include_descendents=True)

        self.find_element_with_text('Need Help?', xpath=f'{plugin_xpath}//*', include_descendents=True)
