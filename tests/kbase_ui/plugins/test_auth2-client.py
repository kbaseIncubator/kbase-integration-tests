from tests.kbase_ui.plugins.PluginBase import PluginBase


class AuthTest(PluginBase):
    def test_unauthenticated_login_page(self):
        self.navigate('login')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'KBase Sign In')
        self.wait_for_title('KBase Sign In | KBase')

        self.switch_to_iframe()

        plugin_xpath = '//*[@data-plugin="auth2-client"]'

        def signin_button_xpath(name):
            return f'{plugin_xpath}//*[@data-k-b-testhook-component="signin-button"][@data-k-b-testhook-name="{name}"]'

        # TODO: plugin testhook is nested inside the plugin!
        self.find_element_with_text('Welcome to KBase')

        self.wait_for_visibility_xpath(signin_button_xpath('google'))
        self.wait_for_visibility_xpath(signin_button_xpath('orcid'))
        self.wait_for_visibility_xpath(signin_button_xpath('globus'))

        self.wait_for_visibility_xpath(f'{plugin_xpath}//*[@data-k-b-testhook-button="signup"]')

        self.find_element_with_text('Need Help?', xpath=f'{plugin_xpath}//*')

    def test_unauthenticated_signedout_page(self):
        self.navigate('auth2/signedout')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Signed Out')
        self.wait_for_title('Signed Out | KBase')

        self.switch_to_iframe()

        plugin_xpath = '//*[@data-plugin="auth2-client"]'

        def signin_button_xpath(name):
            return f'{plugin_xpath}//*[@data-k-b-testhook-component="signin-button"][@data-k-b-testhook-name="{name}"]'

        # TODO: plugin testhook is nested inside the plugin!
        self.find_element_with_text('You are signed out of KBase.')

        # Make sure the identity provider log out links are available with the correct links
        google_sign_out_link = self.find_element_with_text('Log out from Google')
        self.assertEqual(google_sign_out_link.get_dom_attribute('href'), 'https://accounts.google.com/Logout')
        self.assertEqual(google_sign_out_link.get_dom_attribute('target'), '_blank')

        orcid_sign_out_link = self.find_element_with_text('Log out from ORCiD')
        self.assertEqual(orcid_sign_out_link.get_dom_attribute('href'), 'https://www.orcid.org/signout')
        self.assertEqual(orcid_sign_out_link.get_dom_attribute('target'), '_blank')

        globus_sign_out_link = self.find_element_with_text('Log out from Globus')
        self.assertEqual(globus_sign_out_link.get_dom_attribute('href'), 'https://www.globus.org/app/logout')
        self.assertEqual(globus_sign_out_link.get_dom_attribute('target'), '_blank')
