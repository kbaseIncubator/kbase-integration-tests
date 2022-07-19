from tests.kbase_ui.plugins.PluginBase import PluginBase


class AuthTest(PluginBase):

    def test_unauthenticated_signedout_page(self):
        self.navigate('auth2/signedout')

        # Make sure the default title appears
        self.find_heading(1, 'Signed Out')
        # self.wait_for_text('component', 'title', 'Signed Out')
        self.wait_for_title('Signed Out | KBase')

        self.switch_to_iframe()

        plugin_xpath = '//*[@data-plugin="auth2-client"]'

        def signin_button_xpath(name):
            return f'{plugin_xpath}//*[@data-k-b-testhook-component="signin-button"][@data-k-b-testhook-name="{name}"]'

        # TODO: plugin testhook is nested inside the plugin!
        self.find_element_with_text('You are signed out of KBase.')

        # Make sure the identity provider log out links are available with the correct links
        # Note that we need to use descendent text nodes, but pin the element to the link.
        # Couldn't figure out a way of concatenating text nodes in xpath 1.0 (in which case the role
        # could be omitted.)
        google_sign_out_link = self.find_element_with_text('Log out from Google', xpath='//*[@role="link"]',
                                                           include_descendents=True)
        self.assertEqual(google_sign_out_link.get_dom_attribute('href'), 'https://accounts.google.com/Logout')
        self.assertEqual(google_sign_out_link.get_dom_attribute('target'), '_blank')

        orcid_sign_out_link = self.find_element_with_text('Log out from ORCID', xpath='//*[@role="link"]',
                                                          include_descendents=True)
        self.assertEqual(orcid_sign_out_link.get_dom_attribute('href'), 'https://www.orcid.org/signout')
        self.assertEqual(orcid_sign_out_link.get_dom_attribute('target'), '_blank')

        globus_sign_out_link = self.find_element_with_text('Log out from Globus', xpath='//*[@role="link"]',
                                                           include_descendents=True)
        self.assertEqual(globus_sign_out_link.get_dom_attribute('href'), 'https://www.globus.org/app/logout')
        self.assertEqual(globus_sign_out_link.get_dom_attribute('target'), '_blank')
