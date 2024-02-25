from tests.kbase_ui.auth.AuthBase import AuthBase


class AccountTest(AuthBase):
    def test_linked_sign_in_accounts(self):
        label = "Linked Sign-In Accounts"
        # TODO: we can also navigate directly to the tab...
        self.accounts_manager('Update Your Account')
        tab = self.assert_tab(label, is_active=False, exact=True)
        tab.click()
        self.assert_tab(label, is_active=True, exact=True)

        # Currently linked accounts
        linked_accounts_well = self.find_well("Currently Linked Accounts")
        self.assert_table_cell_text("Provider", 1, "Globus", start_from=linked_accounts_well)
        self.assert_table_cell_text(
            "Username", 1, "kbaseuitest@globusid.org", start_from=linked_accounts_well
        )
        self.assert_table_cell_text("Action", 1, "Unlink", start_from=linked_accounts_well)
        self.assert_table_cell_text("Action", 1, "Unlink", start_from=linked_accounts_well)
