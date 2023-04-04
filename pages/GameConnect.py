
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
from pages.BasePage import BasePage
from pages.GameBase import GameBase


class GameConnect(GameBase):
    ITEM_TO_CONNECT = (By.CSS_SELECTOR, '.join-item')

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.CONNECT_GAME_URL)

    def get_item(self):
        return self.driver.find_elements(*self.ITEM_TO_CONNECT)

    def connect(self):
        items = self.get_item()
        self.drag_and_drop(items[1], items[3])
        self.drag_and_drop(items[2], items[4])
        self.drag_and_drop(items[8], items[7])
