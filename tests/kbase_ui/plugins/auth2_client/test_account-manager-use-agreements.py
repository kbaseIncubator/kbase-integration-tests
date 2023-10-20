from selenium.webdriver.common.by import By

from tests.kbase_ui.plugins.auth2_client.Auth2ClientBase import Auth2ClientBase


class AccountTest(Auth2ClientBase):

    def test_data_policy(self):
        self.accounts_manager()

        self.select_tab('Use Agreements', is_active=False)

        # Through the policy title, ensure that the related content is present and
        # grouped with it.
        policy_tab, panel = self.select_tab('KBase Data Policy', xpath='//*', is_active=False, include_descendents=True)

        self.assertIsNotNone(
            # self.find_element_with_text('version: 1',
            #                             start_from=policy_tab,
            #                             include_descendents=True))
            self.find_element_with_this_and_that('version', '1',
                                        start_from=policy_tab,
                                        include_descendents=True))
        self.assertIsNotNone(
            # self.find_element_with_text('published: 1/1/15',
            #                             start_from=policy_tab,
            #                             include_descendents=True))
            self.find_element_with_this_and_that('published', '1/1/15',
                                        start_from=policy_tab,
                                        include_descendents=True))
        self.assertIsNotNone(
            self.find_element_with_this_and_that('agreed', '1/6/20',
                                        start_from=policy_tab,
                                        include_descendents=True))
            # self.find_element_with_text('agreed: 1/6/20, 1:48 PM',
            #                             start_from=policy_tab,
            #                             include_descendents=True))

        self.find_element_with_text('Data Policy', start_from=panel)

        self.find_element_containing_text('KBase conforms to the',
                                          start_from=panel)

    def select_tab(self, label, xpath='', is_active=False, start_from=None, include_descendents=False):
        if include_descendents:
            text_operator = '.'
        else:
            text_operator = 'text()'
        label_xpath = f'{xpath}[contains({text_operator}, "{label}")]'
        tab = self.assert_tab2(label_xpath, is_active=is_active)
        if not is_active:
            tab.click()
            tab = self.assert_tab2(label_xpath, is_active=True)
        tab_id = tab.get_attribute('id')
        panel = self.browser.find_element(By.XPATH, f'//*[@role="tabpanel"][@aria-labeledby="{tab_id}"]')
        return [tab, panel]

    def test_use_agreement(self):
        self.accounts_manager()

        main_tab, main_panel = self.select_tab('Use Agreements', is_active=False)

        # Through the policy title, ensure that the related content is present and
        # grouped with it.
        # self.assert_tab2('//*[text()="KBase Data Policy"]', is_active=True)

        # TODO: Should not depend on whether active or not, here at least.
        # In any case, this tab should be active by default
        use_agreement_tab, panel = self.select_tab('KBase Use Agreement', xpath='//*', is_active=True, include_descendents=True)

        self.assertIsNotNone(
            self.find_element_with_this_and_that('version', '1',
                                        start_from=use_agreement_tab,
                                        include_descendents=True))
        self.assertIsNotNone(
            self.find_element_with_this_and_that('published', '1/1/15',
                                        start_from=use_agreement_tab,
                                        include_descendents=True))
        self.assertIsNotNone(
            self.find_element_with_this_and_that('agreed', '1/6/20',
                                        start_from=use_agreement_tab,
                                        include_descendents=True))

        self.find_element_with_text('Terms and Conditions', start_from=panel)

        self.find_element_containing_text('As a condition of your use',
                                          start_from=panel)

    def test_use_agreements_help(self):
        self.accounts_manager()
        tab = self.assert_tab('Use Agreements', is_active=False)
        tab.click()
        self.assert_tab('Use Agreements', is_active=True)

        self.assert_help_tab([
            'This tab lists the Use Policies you have agreed to during signup or signin to KBase.'
        ])
