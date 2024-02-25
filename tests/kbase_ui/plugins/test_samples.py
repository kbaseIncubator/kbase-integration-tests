from tests.kbase_ui.plugins.PluginBase import PluginBase


class SamplesTest(PluginBase):
    def test_authenticated_sample_view(self):
        sample_name = '0408-FW021.46.11.27.12.02'
        sample_id = '1e476e13-20be-4133-bf8a-6a5681423070'
        self.login_navigate(f'samples/view/{sample_id}/1')

        # Make sure the default title appears
        title = f'KBase: Sample View for "{sample_name}"'
        self.wait_for_title(title)

    def test_unauthenticated_sample_view(self):
        sample_id = '1e476e13-20be-4133-bf8a-6a5681423070'
        plugin_path = f'samples/view/{sample_id}/1'

        self.navigate(plugin_path)

        self.switch_to_kbase_ui_plugin_iframe()

        error_message_xpath = '//*[@class="ant-result-subtitle"]'
        error_message = 'Sample service error code 20000 Unauthorized: Anonymous users cannot read sample 1e476e13-20be-4133-bf8a-6a5681423070'
        self.wait_for_text_xpath(error_message_xpath, error_message)
