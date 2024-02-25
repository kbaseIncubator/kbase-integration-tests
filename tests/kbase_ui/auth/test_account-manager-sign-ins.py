from tests.kbase_ui.auth.AuthBase import AuthBase


class AccountTest(AuthBase):
    def test_active_signin_sessions_tab(self):
        label = "Active Sign-In Sessions"
        # TODO: we can also navigate directly to the tab...
        self.accounts_manager('Update Your Account')
        tab = self.assert_tab(label, is_active=False, exact=True)
        tab.click()
        self.assert_tab(label, is_active=True, exact=True)


        well = self.find_well("Your Current Login Session")

        # this is an example of a table test for a specific sign-in.
        # However, cannot be relied upon, should be obvious why.
        # Rather we'd apply something more complicated, but uniform, like regex
        # self.assert_table(current_panel, [
        #     ['Jul 18, 2022 at 9:40am', '13d 11h 7m', 'Safari15.5', 'Mac OS X10.15.7', '71.231.144.187']
        # ])
        self.assert_table2(header=[
            'Created', 'Expires', 'Browser', 'Operating System', 'IP Address'
        ], row_count=1, start_from=well)

        # the other sessions panel
        # note that the test account should not have any other sign-in sessions!
        well = self.find_well("Other Login Sessions")
        self.find_element_containing_text('You do not have any additional active sign-in sessions.',
                                          start_from=well)
