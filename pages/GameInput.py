import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
from pages.GameBase import GameBase


class GameInputWorksheet(GameBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.open_ws()

    def open_ws(self):
        self.driver.get(TestData.INPUT_GAME_URL)

    def get_input_boxes(self):
        return self.driver.find_elements(*self.INPUT_BOX)

    def fill_input(self):
        input_boxes = self.get_input_boxes()
        input_boxes[1].send_keys(2)
        input_boxes[2].send_keys(2)
        input_boxes[3].send_keys(4)

    def clear_input(self):
        inputed_boxes = self.get_input_boxes()
        inputed_boxes[1].clear()
        inputed_boxes[2].clear()
        inputed_boxes[3].clear()

    def get_interactive_box_location(self):
        locations = []
        input_boxes = self.get_input_boxes()
        for i in input_boxes:
            locations.append(i.location)
        return locations






