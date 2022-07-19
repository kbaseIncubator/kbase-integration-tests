from tests.kbase_ui.plugins.auth2_client.Auth2ClientBase import Auth2ClientBase


class AccountTest(Auth2ClientBase):
    def test_sign_ins_tab(self):
        self.accounts_manager()
        tab = self.assert_tab('Sign-Ins', is_active=False)
        tab.click()
        self.assert_tab('Sign-Ins', is_active=True)

        sign_ins_tab = self.assert_tab('Manage Your Sign-Ins', is_active=True)

        # the  current token panel
        current_panel = self.find_panel('Your Current Sign-In')

        # this is an example of a table test for a specific sign-in.
        # However, cannot be relied upon, should be obvious why.
        # Rather we'd apply something more complicated, but uniform, like regex
        # self.assert_table(current_panel, [
        #     ['Jul 18, 2022 at 9:40am', '13d 11h 7m', 'Safari15.5', 'Mac OS X10.15.7', '71.231.144.187']
        # ])
        self.assert_table2(header=[
            'Created', 'Expires', 'Browser', 'Operating System', 'IP Address'
        ], row_count=1, start_from=current_panel)

        # the other sessions panel
        other_panel = self.find_panel('Other Sign-In Sessions')
        self.find_element_containing_text('You do not have any additional active sign-in sessions.',
                                          start_from=other_panel)

    def test_help_tab(self):
        self.accounts_manager()
        tab = self.assert_tab('Sign-Ins', is_active=False, exact=True)
        tab.click()
        self.assert_tab('Sign-Ins', is_active=True, exact=True)

        self.assert_help_tab([
            'A sign-in session is removed when you logout'
        ])
