from tests.kbase_ui.plugins.PluginBase import PluginBase


class FeedsTest(PluginBase):
    def test_authenticated_basic(self):
        self.login_navigate('feeds')

        # Make sure the default title appears
        self.wait_for_text('component', 'title', 'Notification Feeds')
        self.wait_for_title('Notification Feeds | KBase')

        self.switch_to_iframe()

        feeds_tab = self.kbase_testhook([['element', 'tabs']])
        global_tab = f'{feeds_tab}//*[@data-name="global"]'
        self.wait_for_text_xpath(global_tab, 'KBase Announcements')

        user_tab = f'{feeds_tab}//*[@data-name="user"]'
        self.wait_for_text_xpath(user_tab, 'KBase UI Test User')

        org_tab = f'{feeds_tab}//*[@data-name="anorg"]'
        self.wait_for_text_xpath(org_tab, 'an org')

    def test_unauthenticated(self):
        self.auth_blocked_plugin('feeds')
