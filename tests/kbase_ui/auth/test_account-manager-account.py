from tests.kbase_ui.auth.AuthBase import AuthBase


class AccountTest(AuthBase):
    def test_authenticated_initial_page(self):
        # Navigates to the account manager and moves to context
        # into the iframe.
        label = 'Update Your Account'
        self.accounts_manager(label)

        # self.assert_tab('Account', is_active=True)
        self.assert_tab(label, is_active=True)

        self.wait_for_labeled_input('Your Name', 'KBase UI Test User')
        self.wait_for_labeled_input('E-Mail Address', 'eapearson+kbaseuitest@lbl.gov')
        self.assert_labeled_text('Username', 'kbaseuitest')
        self.assert_labeled_text('Account Created', 'Jan 6, 2020 at 1:48pm')

        # # Note that we need a regex here since the last sign in will change
        # # over time, reflecting when the last token was created for the test account.
        # # like: 22 hours ago (Jul 18, 2022 at 9:40am)
        self.assert_labeled_text('Last Sign In',
                                 '^.+ ago [(][A-Z][a-z][a-z] [0-9]+, 20[2-9][0-9] at [1-9][0-9]*:[0-9][0-9](?:am)|(?:pm)[)]$',
                                 comparison='regex')

    def test_unauthenticated(self):
        self.navigate('account')
        self.auth_blocked('account', 'Account Manager')
