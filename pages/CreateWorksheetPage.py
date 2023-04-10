import time
from math import isclose

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Config.config import TestData
from pages.BasePage import BasePage


class CreateWorksheetPage(BasePage):
    # Locators
    EDIT_WORKSHEET_BUTTON = (
        By.CSS_SELECTOR, "div.list-action-button > div:nth-child(1)")
    MAKE_INTERACTIVE_BUTTON = (
        By.CSS_SELECTOR, "div.list-action-button > div:nth-child(2)")
    TRY_IT_OUT_BUTTON = (
        By.CSS_SELECTOR, "div.list-action-button > div:nth-child(3)")
    RED_SAVE_BUTTON = (
        (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(5)"))
    UPLOAD_IMAGE_BUTTON = (
        By.CSS_SELECTOR, "div.canvas-pages > div:nth-child(2) > div > label > input[type=file]")

    EXAMPLE_TEMPLATE = (
        By.CSS_SELECTOR, ".template-resource-item:nth-child(1)")
    MESSAGE_BAR = (
        By.CSS_SELECTOR, "#app > div.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter.css-1ozswge")

    SAVE_POP_UP = (
        By.CSS_SELECTOR, "body > div.MuiDialog-root.popup-save-worksheet.MuiModal-root.css-126xj0f")
    UNDO_REDO_BUTTON = (By.CSS_SELECTOR, "div.undo-redo-button")

    # SAVE_POPUP_CONTAINER
    WS_NAME = (By.CSS_SELECTOR, "input#ws-name")
    BLUE_SAVE_BUTTON = (By.CSS_SELECTOR, ".save-btn")

    SHARE_POPUP_CONTAINER = (By.CSS_SELECTOR, ".shared-popup-container")

    # # Login
    USER = (By.CSS_SELECTOR, ".user")

    # Zoom
    ZOOM_BUTTON = (By.CSS_SELECTOR, )
    ZOOM_PANEL = (By.CSS_SELECTOR, "zoom-panel")
    ZOOM_VALUE_ITEM = {45: (By.CSS_SELECTOR, "div.zoom-panel > div:nth-child(1)"),
                       200: (By.CSS_SELECTOR, "div.zoom-panel > div:nth-child(7)")}

    # Add Page
    ADD_PAGE_BUTTON = (By.CSS_SELECTOR, ".add-page")
    ADD_PAGE_ICON = (
        By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(7)")
    
    # Tag Bar
    TAG_BAR_ICON =(By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(8)")

    # Duplicate
    DUPLICATE_ICON =(By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(5)")

    # Scroll
    SCROLL_TO_TOP_BUTTON = (By.CSS_SELECTOR, ".scroll-to-top-button")

    PAGE = (By.CSS_SELECTOR, "div.canvas-pages")
    PAGE_WITH_WS = (By.CSS_SELECTOR,
                    "div.canvas-pages > div.switch-button-eraser")
    RIGHT_CONTAINER = (By.CSS_SELECTOR, ".simplebar-content-wrapper")

    def __init__(self, driver):
        super().__init__(driver)

    def open_browser(self):
        self.driver.get(TestData.CREATE_WORKSHEET_URL)

    def click_make_interactive_button(self):
        self.do_lick(self.MAKE_INTERACTIVE_BUTTON)

    def upload_file(self):
        upload_button = self.driver.find_element(*self.UPLOAD_IMAGE_BUTTON)
        upload_button.send_keys(TestData.PATH_TO_TEST_FILE)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".canvas-container-0"))
        )

    def get_red_save_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RED_SAVE_BUTTON)
        )

    def click_red_save_button(self):
        self.get_red_save_button().click()

    def input_ws_name(self):
        name_input_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.WS_NAME)
        )
        name_input_box.send_keys("name")

    def click_blue_save_button(self):
        self.driver.find_element(*self.BLUE_SAVE_BUTTON).click()

    def pick_a_template(self):
        self.driver.find_element(*self.EXAMPLE_TEMPLATE).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".canvas-container-0"))
        )
        time.sleep(2)

    def get_the_message_bar(self):
        return self.driver.find_element(*self.MESSAGE_BAR)

    def get_save_pop_up(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.SAVE_POP_UP)
        )

    def get_shared_popup(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.SHARE_POPUP_CONTAINER)
        )

    def get_undo_redo_btn(self):
        return self.driver.find_elements(*self.UNDO_REDO_BUTTON)

    def undo_redo_btn(self, action, btn):
        undo_redo_btn = self.get_undo_redo_btn()
        undo_btn = undo_redo_btn[0]
        redo_btn = undo_redo_btn[1]
        action_chains = ActionChains(self.driver)

        if action == "hover":
            if btn == "redo":
                action_chains.move_to_element(redo_btn).perform()
            else:
                action_chains.move_to_element(undo_btn).perform()
        else:
            redo_btn.click() if btn == "redo" else undo_btn.click()

    def change_ws_size(self, size):
        arrow = self.driver.find_element(
            By.CSS_SELECTOR, "div.zoom-value-container > img")
        arrow.click()
        self.driver.find_element(*self.ZOOM_VALUE_ITEM[size]).click()
        time.sleep(2)

    def add_page_with_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RIGHT_CONTAINER)
        )
        add_page_btn = self.driver.find_element(*self.ADD_PAGE_BUTTON)
        add_page_btn.click()

    def add_page_with_icon(self):
        add_page_icon = self.driver.find_element(*self.ADD_PAGE_ICON)
        add_page_icon.click()

    def scroll_to_bottom(self):
        self.driver.execute_script("let element = document.getElementsByClassName('simplebar-content-wrapper')[0];"
                                   "element.scroll({ top: element.scrollHeight, behavior: 'smooth' });")

    def get_scroll_to_top_button(self):
        return self.driver.find_element(*self.SCROLL_TO_TOP_BUTTON)

    def click_scroll_to_top_button(self):
        btn = self.get_scroll_to_top_button()
        btn.click()

    def get_page_with_template(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.PAGE_WITH_WS)
        )

    def is_template_display(self):
        return self.is_display(self.PAGE_WITH_WS)

    def get_page_size(self):
        page = self.driver.find_element(*self.PAGE)
        return page.size

    def get_scroll_position(self):
        return self.driver.execute_script("let element = document.getElementsByClassName('simplebar-content-wrapper')[0];return element.scrollTop"
                                          )

    def get_page_position(self):
        return self.driver.execute_script(f"let element = document.getElementsByClassName('canvas-pages');let lastElement=element[element.length-1];return lastElement.getBoundingClientRect();")

    def is_up_button_display(self):
        return self.is_display(self.SCROLL_TO_TOP_BUTTON)


    # Tag bar
    def hover_on_tag_bar_icon(self):
        tag_bar_icon = self.driver.find_element(*self.TAG_BAR_ICON)
        self.hover(tag_bar_icon)

    def click_on_tag_bar_icon(self):
        self.do_lick(self.TAG_BAR_ICON)

    # Duplicate
    def click_duplicate_icon(self):
        self.do_lick(self.DUPLICATE_ICON)