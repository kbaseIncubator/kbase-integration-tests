from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class PluginBase(KBaseUIBase):
    def auth_blocked_plugin(self, plugin_path):
        self.navigate(plugin_path)

        self.switch_to_iframe()

        request_path = self.kbase_testhook(
            [['plugin', 'auth2-client'], ['component', 'login-view'], ['field', 'requested-path']])
        self.wait_for_text_xpath(request_path, plugin_path)
