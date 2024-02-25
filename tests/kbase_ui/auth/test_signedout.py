from selenium.webdriver.common.by import By

from tests.kbase_ui.plugins.PluginBase import PluginBase


class AuthTest(PluginBase):

    def test_unauthenticated_signedout_page(self):
        self.navigate('signedout')

                # Make sure the default title appears
        self.wait_for_title('KBase: Signed Out')

        self.switch_to_kbase_ui_iframe()

        # self.find_heading(1, 'Signed Out')

        well = self.find_well('You are signed out of KBase.')

        google_link = well.find_element(By.XPATH, '//*[@role="link" and contains(., "Google")]')
        assert google_link.get_attribute('href') == 'https://accounts.google.com/Logout'
        assert google_link.get_attribute('target') == '_blank'

        orcid_link = well.find_element(By.XPATH, '//*[@role="link" and contains(., "ORCID")]')
        assert orcid_link.get_attribute('href') == 'https://www.orcid.org/signout'
        assert orcid_link.get_attribute('target') == '_blank'

        globus_link = well.find_element(By.XPATH, '//*[@role="link" and contains(., "Globus")]')
        assert globus_link.get_attribute('href') == 'https://app.globus.org/logout'
        assert globus_link.get_attribute('target') == '_blank'
