from tests.kbase_ui.plugins.PluginBase import PluginBase


class AccountTest(PluginBase):

    def accounts_manager(self):
        self.login_navigate('auth2/account')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Account Manager')
        self.wait_for_title('Account Manager | KBase')

        self.switch_to_iframe()

    def assert_tab(self, label, is_active=False):
        label = self.wait_for_element_with_text('', label)
        tab = self.get_parent(label)
        self.assertRegex(tab.get_attribute('class'), '-tab')
        if is_active:
            self.assertRegex(tab.get_attribute('class'), '-active')
        return tab

    def test_authenticated_initial_page(self):
        self.accounts_manager()

        self.assert_tab('Account', is_active=True)

        update_account_label = self.wait_for_element_with_text('', 'Update Your Account')
        update_account_tab = self.get_parent(self.get_parent(update_account_label))
        self.assertRegex(update_account_tab.get_attribute('class'), 'active')

        self.wait_for_labeled_input('', 'Name', 'KBase UI Test User')
        self.wait_for_labeled_input('', 'E-Mail', 'eapearson+kbaseuitest@lbl.gov')
        self.wait_for_labeled_text('', 'Username', 'kbaseuitest')
        self.wait_for_labeled_text('', 'Account Created', 'Jan 6, 2020 at 1:48pm')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('auth2/account')

    def test_linked_sign_in_accounts(self):
        self.accounts_manager()
        tab = self.assert_tab('Linked Sign-In Accounts', is_active=False)
        tab.click()
        self.assert_tab('Linked Sign-In Accounts', is_active=True)

        # the other type of tab (unify them!?!)
        update_account_label = self.wait_for_element_with_text('', 'Manage Your Linked Sign-in Accounts')
        update_account_tab = self.get_parent(self.get_parent(update_account_label))
        self.assertRegex(update_account_tab.get_attribute('class'), 'active')

        self.wait_for_table_cell_text('', 'Provider', 1, 'Globus')
        self.wait_for_table_cell_text('', 'Username', 1, 'kbaseuitest@globusid.org')
        self.wait_for_table_cell_text('', 'Action', 1, 'Unlink')
