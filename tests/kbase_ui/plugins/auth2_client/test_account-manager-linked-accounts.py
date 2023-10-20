from tests.kbase_ui.plugins.auth2_client.Auth2ClientBase import Auth2ClientBase


class AccountTest(Auth2ClientBase):
    def test_linked_sign_in_accounts(self):
        self.accounts_manager()
        tab = self.assert_tab("Linked Sign-In Accounts", is_active=False, exact=True)
        tab.click()
        self.assert_tab("Linked Sign-In Accounts", is_active=True, exact=True)

        self.assert_tab("Manage Your Linked Sign-In Accounts", is_active=True)

        # Currently linked accounts
        current_panel = self.find_panel("Currently Linked Accounts")

        self.assert_table_cell_text("Provider", 1, "Globus", start_from=current_panel)
        self.assert_table_cell_text(
            "Username", 1, "kbaseuitest@globusid.org", start_from=current_panel
        )
        self.assert_table_cell_text("Action", 1, "Unlink", start_from=current_panel)

    def test_linked_sign_in_accounts_help(self):
        self.accounts_manager()
        tab = self.assert_tab("Linked Sign-In Accounts", is_active=False, exact=True)
        tab.click()
        self.assert_tab("Linked Sign-In Accounts", is_active=True, exact=True)

        self.assert_help_tab(
            [
                "This tab provides access",
                "You may unlink any linked sign-in account from",
            ]
        )
