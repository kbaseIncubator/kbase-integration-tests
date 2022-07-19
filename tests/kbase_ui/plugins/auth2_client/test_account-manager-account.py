from tests.kbase_ui.plugins.auth2_client.Auth2ClientBase import Auth2ClientBase


class AccountTest(Auth2ClientBase):
    def test_authenticated_initial_page(self):
        # Navigates to the account manager and moves to context
        # into the iframe.
        self.accounts_manager()

        self.assert_tab('Account', is_active=True)
        self.assert_tab('Update Your Account', is_active=True)

        self.wait_for_labeled_input('Name', 'KBase UI Test User')
        self.wait_for_labeled_input('E-Mail', 'eapearson+kbaseuitest@lbl.gov')
        self.assert_labeled_text('Username', 'kbaseuitest')
        self.assert_labeled_text('Account Created', 'Jan 6, 2020 at 1:48pm')

        # Note that we need a regex here since the last sign in will change
        # over time, reflecting when the last token was created for the test account.
        # like: 22 hours ago (Jul 18, 2022 at 9:40am)
        self.assert_labeled_text('Last Sign In',
                                 '^.+ ago [(][A-Z][a-z][a-z] [0-9]+, 20[2-9][0-9] at [1-9][0-9]*:[0-9][0-9](?:am)|(?:pm)[)]$',
                                 comparison='regex')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('auth2/account')

    def test_help_tab(self):
        self.accounts_manager()
        self.assert_tab('Account', is_active=True, exact=True)

        self.assert_help_tab([
            'You may view and edit edit your basic account information here.'
        ])
