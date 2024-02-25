from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.kbase_ui.KBaseUIBase import KBaseUIBase


class DefaultPathTest(KBaseUIBase):
    def test_authenticated_default_page(self):
        self.login_navigate("")

        # self.wait_for_titles('Narratives Navigator')
        # This currently ends up on the Navigator, which does not use
        # the same layout as kbase-ui, so let's roll by hand.
        expected_title = "Narrative Navigator"
        self.assert_title(expected_title)

        # self.wait.until(
        #     expected_conditions.text_to_be_present_in_element(
        #         (By.XPATH, "//h1"), expected_title
        #     )
        # )