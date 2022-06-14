from tests.kbase_ui.plugins.PluginBase import PluginBase


class AccountTest(PluginBase):

    def accounts_manager(self):
        self.login_navigate('auth2/account')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Account Manager')
        self.wait_for_title('Account Manager | KBase')

        self.switch_to_iframe()

    def assert_tab(self, label, is_active=False):
        label = self.find_element_with_text(label)
        tab = self.get_parent(label)
        self.assertRegex(tab.get_attribute('class'), '-tab')
        if is_active:
            self.wait_for_attribute_contains(tab, 'class', '-active')
            # self.assertRegex(tab.get_attribute('class'), '-active')
        return tab

    def test_authenticated_initial_page(self):
        self.accounts_manager()

        self.assert_tab('Account', is_active=True)

        update_account_label = self.find_element_with_text('Update Your Account')
        update_account_tab = self.get_parent(self.get_parent(update_account_label))
        self.assertRegex(update_account_tab.get_attribute('class'), 'active')

        self.wait_for_labeled_input('Name', 'KBase UI Test User')
        self.wait_for_labeled_input('E-Mail', 'eapearson+kbaseuitest@lbl.gov')
        self.wait_for_labeled_text('Username', 'kbaseuitest')
        self.wait_for_labeled_text('Account Created', 'Jan 6, 2020 at 1:48pm')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('auth2/account')

    def test_linked_sign_in_accounts(self):
        self.accounts_manager()
        tab = self.assert_tab('Linked Sign-In Accounts', is_active=False)
        tab.click()
        self.assert_tab('Linked Sign-In Accounts', is_active=True)

        # the other type of tab (unify them!?!)
        update_account_label = self.find_element_with_text('Manage Your Linked Sign-in Accounts')
        update_account_tab = self.get_parent(self.get_parent(update_account_label))
        self.assertRegex(update_account_tab.get_attribute('class'), 'active')

        self.wait_for_table_cell_text('Provider', 1, 'Globus')
        self.wait_for_table_cell_text('Username', 1, 'kbaseuitest@globusid.org')
        self.wait_for_table_cell_text('Action', 1, 'Unlink')

    def test_data_policy(self):
        self.accounts_manager()
        tab = self.assert_tab('Use Agreements', is_active=False)
        tab.click()
        self.assert_tab('Use Agreements', is_active=True)

        # Through the policy title, ensure that the related content is present and
        # grouped with it.
        policy_title = self.find_element_with_text('KBase Data Policy')
        policy = self.get_parent(policy_title)
        self.assertIsNotNone(policy)
        self.assertIsNotNone(self.find_by_text('version: 1', start_from=policy))
        self.assertIsNotNone(self.find_by_text('published: 12/31/2014', start_from=policy))
        self.assertIsNotNone(self.find_by_text('agreed: 1/6/2020', start_from=policy))

        # Initially, no agreement is shown.
        message = self.find_by_text('Select an existing agreement on the left to view it here')
        self.assertIsNotNone(message)
        content_area = self.get_parent(message)
        self.assertIsNotNone(content_area)
        content_area_id = content_area.get_attribute('id')

        # Select the policy, it should appear within the page. Look for it by the title, and ensure
        # that some choice bits are present within the same grouping.

        # First there
        policy_button = self.get_parent(policy)
        policy_button.click()

        # Find the policy area by the expected text
        # Then we can inspect bits within it.
        # policy_content = self.wait_for_text_xpath(f'//*', 'Data Policy')
        self.wait_for_text_xpath(f'//*[@id="{content_area_id}"]', 'Data Policy')

        # subtitle
        self.assertIsNotNone(self.find_element_with_text('Data Policies', start_from=content_area))

        # A paragraph
        self.assertIsNotNone(
            self.find_element_containing_text('Genomic Science Program', start_from=content_area))

        self.assertIsNotNone(
            self.find_element_containing_text('All data uploaded by users', start_from=content_area))

    def test_use_agreement(self):
        self.accounts_manager()
        tab = self.assert_tab('Use Agreements', is_active=False)
        tab.click()
        self.assert_tab('Use Agreements', is_active=True)

        # Through the policy title, ensure that the related content is present and
        # grouped with it.
        policy_title = self.find_element_with_text('KBase Use Agreement')
        policy = self.get_parent(policy_title)
        self.assertIsNotNone(policy)
        self.assertIsNotNone(self.find_by_text('version: 1', start_from=policy))
        self.assertIsNotNone(self.find_by_text('published: 12/31/2014', start_from=policy))
        self.assertIsNotNone(self.find_by_text('agreed: 1/6/2020', start_from=policy))

        # Initially, no agreement is shown.
        message = self.find_by_text('Select an existing agreement on the left to view it here')
        self.assertIsNotNone(message)
        content_area = self.get_parent(message)
        self.assertIsNotNone(content_area)
        content_area_id = content_area.get_attribute('id')

        # Select the policy, it should appear within the page. Look for it by the title, and ensure
        # that some choice bits are present within the same grouping.

        # First there
        policy_button = self.get_parent(policy)
        policy_button.click()

        # Find the policy area by the expected text
        # Then we can inspect bits within it.
        # policy_content = self.wait_for_text_xpath(f'//*', 'Data Policy')
        self.wait_for_text_xpath(f'//*[@id="{content_area_id}"]', 'Terms and Conditions')

        # subtitle
        self.assertIsNotNone(self.find_element_with_text('Prohibited Behavior', start_from=content_area))

        # A paragraph
        self.assertIsNotNone(
            self.find_element_containing_text('As a condition of your use of KBase', start_from=content_area))

        self.assertIsNotNone(
            self.find_element_containing_text('KBase does not guarantee long-term retention of user uploaded data',
                                              start_from=content_area))

    def test_use_agreements_help(self):
        self.accounts_manager()
        tab = self.assert_tab('Use Agreements', is_active=False)
        tab.click()
        self.assert_tab('Use Agreements', is_active=True)

        # TODO:
        # since the tab is populated with an icon, we can't select it by content,
        # but we can select it as the tab just to the right of the main tab.
