from selenium.webdriver.common.by import By

from tests.kbase_ui.auth.AuthBase import AuthBase


class AccountTest(AuthBase):
    def test_terms_and_conditions(self):
        label = "Terms and Conditions"
        # TODO: we can also navigate directly to the tab...
        self.accounts_manager('Update Your Account')
        tab = self.assert_tab(label, is_active=False, exact=True)
        tab.click()
        self.assert_tab(label, is_active=True, exact=True)
        well = self.find_well("Terms and Conditions")
        self.wait_for_labeled_text2('Version', '2', within=well)
        self.wait_for_labeled_text2('Published At', 'Apr 1, 2023 at 0:00am', within=well)
        self.wait_for_labeled_text2('Agreed At', 'Nov 9, 2023 at 9:57am', within=well)
        self.wait_for_labeled_text2('Agreed At', 'Nov 9, 2023 at 9:57am', within=well)
        self.wait_for_labeled_text2('Agreed At', 'Nov 9, 2023 at 9:57am', within=well)
