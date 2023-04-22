import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Utilities.customLog import LogGen



class BasePage:
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def is_page_loaded(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        return bool(element)

    def is_display(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def do_lick(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(element)

    def escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE)
        actions.perform()

    def get_location(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.location
    
    def get_element_location(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        rect = self.driver.execute_script(f"let element = document.querySelector('{locator[1]}');return element.getBoundingClientRect();")
        return {'x': rect['x'], 'y': rect['y']}

    def is_correct_location(self, location, actual_location):
        tolerance = 20
        if actual_location['x'] - tolerance <= location['x'] <= actual_location['x'] + tolerance and actual_location['y'] - tolerance <= location['y'] <= actual_location['y'] + tolerance:
            return True
        else:
            return False

    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def drag_to_location(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y).perform()

    def printCurrentURL(self):
        print(self.driver.current_url)

    def switchTab(self, tab_index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[tab_index])


    def hover(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
















