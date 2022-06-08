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
        self.wait_for_element_with_text('', 'Welcome to KBase')

        self.wait_for_visibility_xpath(signin_button_xpath('google'))
        self.wait_for_visibility_xpath(signin_button_xpath('orcid'))
        self.wait_for_visibility_xpath(signin_button_xpath('globus'))

        self.wait_for_visibility_xpath(f'{plugin_xpath}//*[@data-k-b-testhook-button="signup"]')

        self.wait_for_element_with_text(plugin_xpath, 'Need Help?')
