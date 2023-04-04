import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
from Utilities.customLog import LogGen
from pages.BasePage import BasePage
from pages.GameInput import GameInputWorksheet
from pages.CreateWorksheetPage import CreateWorksheetPage


class PreviewPage(BasePage):
    # Locators
    INPUT_BOX = (By.CSS_SELECTOR, ".fill-blank-input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    CUSTOMIZE_BUTTON = (By.CSS_SELECTOR, ".customize-ws")
    PLAY_NOW_BUTTON = (By.CSS_SELECTOR, ".tracking-dont-delete-play-now-button")
    INTERACTIVE_BOX = (By.CSS_SELECTOR, '.fill-blank-input')

    def __init__(self, driver):
        super().__init__(driver)

    def open_browser(self):
        self.driver.get(TestData.PREVIEW_PAGE_URL)

    def click_play_now_button(self):
        class PlayPage(GameInputWorksheet):
            def __init__(self, driver):
                super().__init__(driver)

            def open_ws(self):
                pass

        self.do_lick(self.PLAY_NOW_BUTTON)
        return PlayPage(self.driver)

    def click_customize_button(self):
        self.do_lick(self.CUSTOMIZE_BUTTON)
        return CreateWorksheetPage(self.driver)

    def get_interactive_box_location(self):
        interactive_boxes = self.driver.find_elements(*self.INTERACTIVE_BOX)
        interactive_box_location = []
        for interactive_box in interactive_boxes:
            interactive_box_location.append(interactive_box.location)
        return interactive_box_location
