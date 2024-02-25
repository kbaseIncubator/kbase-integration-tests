from selenium.webdriver.common.by import By

from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class AuthBase(KBaseUIBase):
    def accounts_manager(self, label):
        self.login_navigate('account')
        title = f'Account Manager - {label}'
        self.wait_for_title(f'KBase: {title}')
        self.switch_to_kbase_ui_iframe()

    def assert_tab(self, label, is_active=False, exact=False):
        if is_active:
            hit = self.find_element_with_text(label, xpath='//*[@role="tab" and @aria-selected="true"]',
                                              include_descendents=not exact)
        else:
            hit = self.find_element_with_text(label, xpath='//*[@role="tab" and @aria-selected="false"]',
                                              include_descendents=not exact)

        tab = hit.find_element(By.XPATH, './ancestor-or-self::*[@role="tab"][1]')
        return tab

    def assert_tab2(self, xpath, is_active=False):
        if is_active:
            hit = self.browser.find_element(By.XPATH, f'//*[@role="tab" and @aria-selected="true"]{xpath}')
        else:
            hit = self.browser.find_element(By.XPATH, f'//*[@role="tab" and @aria-selected="false"]{xpath}')
        tab = hit.find_element(By.XPATH, './ancestor-or-self::*[@role="tab"][1]')
        return tab

    def assert_help_tab(self, text_phrases):
        help_tab = self.assert_tab2('/*[@class="fa fa-info-circle"]', is_active=False)
        help_tab.click()
        help_tab = self.assert_tab2('/*[@class="fa fa-info-circle"]', is_active=True)

        panel_id = help_tab.get_attribute('id')

        tab_panel = self.browser.find_element(By.XPATH, f'//*[@role="tabpanel"][@aria-labeledby="{panel_id}"]//*')

        for text_phrase in text_phrases:
            self.find_element_containing_text(text_phrase,
                                              start_from=tab_panel,
                                              include_descendents=True)
