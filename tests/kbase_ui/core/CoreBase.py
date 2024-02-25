from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class CoreBase(KBaseUIBase):
    pass




    

    # def auth_blocked(self, plugin_path):
    #     self.navigate(plugin_path)

    #     # TODO: visually based rather than using hidden testing hooks
    #     # request_path = self.kbase_testhook(
    #     #     [['plugin', 'auth2-client'], ['field', 'requested-path']])
    #     # self.wait_for_text_xpath(request_path, plugin_path)
    #     heading_element = self.wait_for_presence_xpath('//*[@role="heading"]/span')
    #     print('HEADING?', heading_element.text)
    #     self.wait_for_text_xpath('//*[@role="heading"]', 'Sign In Required')


