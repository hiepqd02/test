import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
from pages.GameBase import GameBase
from selenium.webdriver.common.by import By


class GameDragAndDrop(GameBase):
    CUBE = (By.CSS_SELECTOR, 'div#drag7.drag')
    CONE = (By.CSS_SELECTOR, 'div#drag0.drag')
    SPHERE = (By.CSS_SELECTOR, 'div#drag8.drag')
    CYLINDER = (By.CSS_SELECTOR, 'div#drag2.drag')
    RECTANGULAR = (By.CSS_SELECTOR, "div#drag4.drag")
    DROP_BOXES = (By.CSS_SELECTOR, ".drop")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.DRAG_AND_DROP_GAME_URL)
        time.sleep(2)

    def get_cube_shape(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CUBE)
        )

    def get_cone_shape(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONE)
        )

    def get_sphere_shape(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SPHERE)
        )

    def get_rectangular_shape(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RECTANGULAR)
        )

    def get_cylinder_shape(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CYLINDER)
        )

    def get_drop_boxes(self):
        return self.driver.find_elements(*self.DROP_BOXES)

    def get_drop_box_location(self):
        return self.get_location(self.DROP_BOXES)

    def drag_cube_shape(self):
        self.drag(self.get_cube_shape(), 220, 280)
        # self.drag_and_drop(self.get_cube_shape(), self.get_drop_boxes()[1])

    def drag_cone_shape(self):
        self.drag(self.get_cone_shape(), 300,410)



