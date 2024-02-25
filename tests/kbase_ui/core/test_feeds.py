from tests.kbase_ui.core.CoreBase import CoreBase


class FeedsTest(CoreBase):
    def test_authenticated_basic(self):
        self.login_navigate('feeds')

        # Make sure the title appears
        self.assert_title('Notification Feeds')

        # self.switch_to_iframe()

        # TODO: feeds should be refactored to use roles, then we can
        # remove the testhooks.
        # feeds_tab = self.kbase_testhook([['element', 'tabs']])
        # global_tab = f'{feeds_tab}//*[@data-name="global"]'
        # self.wait_for_text_xpath(global_tab, 'KBase Announcements')

        # user_tab = f'{feeds_tab}//*[@data-name="user"]'
        # self.wait_for_text_xpath(user_tab, 'KBase UI Test User')

        # org_tab = f'{feeds_tab}//*[@data-name="anorg"]'
        # self.wait_for_text_xpath(org_tab, 'an org')

    def test_unauthenticated(self):
        self.auth_blocked('feeds', 'Feeds')
