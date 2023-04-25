import time
from math import isclose

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
    
    # Tab Bar
    TAG_BAR_ICON =(By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(8)")
    TAB_BAR_PAGE = (By.CSS_SELECTOR, ".canvas-pages-right-panel")

    # Duplicate
    DUPLICATE_ICON =(By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(5)")
    DUPLICATE_ICON_ON_TAB_BAR = (By.CSS_SELECTOR, "#menu-page-1 > div.hover-container > div.duplicate")
    # Delete
    DELETE_ICON = (By.CSS_SELECTOR, "div.action-panel-container > div > div > div:nth-child(6)")
    DELETE_ICON_ON_TAG_BAR = (By.CSS_SELECTOR, "#menu-page-1 > div.hover-container > div.delete-icon")

    # Scroll
    SCROLL_TO_TOP_BUTTON = (By.CSS_SELECTOR, ".scroll-to-top-button")

    PAGE = (By.CSS_SELECTOR, "div.canvas-pages")
    PAGE_WITH_WS = (By.CSS_SELECTOR,
                    "div.canvas-pages > div.switch-button-eraser")
    PAGE_IN_TAG_BAR = (By.CSS_SELECTOR, ".canvas-pages-right-panel")
    RIGHT_CONTAINER = (By.CSS_SELECTOR, ".simplebar-content-wrapper")


    #Template Menu
    CLOSE_TEMPLATE_MENU = (By.CSS_SELECTOR, ".close-left-content-button") 
    TEMPLATE_TAB = (By.CSS_SELECTOR, "div.left-content-container > div > div:nth-child(1)")
    TEMPLATE_MENU = (By.CSS_SELECTOR, ".left-content-grid")

    TUTORIAL_POPUP = (By.CSS_SELECTOR, ".tutorial-container")

    # before search
    SEARCH_BAR = (By.CSS_SELECTOR, ".search-input > div > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-input > div > div > div > button")

    # after search
    SEARCH_BAR_2 = (By.CSS_SELECTOR, ".control-action > div > div > input")
    SEARCH_BUTTON_2 = (By.CSS_SELECTOR, ".control-action > div > div > div > div:nth-child(2) > button")
    CLOSE_SEARCH = (By.CSS_SELECTOR, ".control-action > div > div > div > div:nth-child(1) > button")
    TEXT_NO_RESULT = (By.CSS_SELECTOR, ".text-no-result")
    TEMPLATE_FOR_SEARCH = [(By.ID, "633d3138a906c33dcb52b04b"), (By.ID, "6385751530e9fd6587fae0ed")]

    LIST_TAG = (By.CSS_SELECTOR, ".list-sub-content-tag")
    NEXT_ARROW_BTN = (By.CSS_SELECTOR, ".arrow-container.next-arrow > div.circle-arrow")
    PREV_ARROW_BTN = (By.CSS_SELECTOR, ".arrow-container.prev-arrow > div.circle-arrow")



    def __init__(self, driver):
        super().__init__(driver)

    def open_browser(self):
        self.driver.get(TestData.CREATE_WORKSHEET_URL)

    def click_make_interactive_button(self):
        self.do_click(self.MAKE_INTERACTIVE_BUTTON)

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
        return WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(self.SAVE_POP_UP)
        )

    def get_shared_popup(self):
        return WebDriverWait(self.driver, 60).until(
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
        time.sleep(5)

    def add_page_with_icon(self):
        add_page_icon = self.driver.find_element(*self.ADD_PAGE_ICON)
        add_page_icon.click()
        time.sleep(5)

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


    # Tab bar
    def hover_on_tag_bar_icon(self):
        tag_bar_icon = self.driver.find_element(*self.TAG_BAR_ICON)
        self.hover(tag_bar_icon)

    def click_on_tag_bar_icon(self):
        self.do_click(self.TAG_BAR_ICON)




    # Duplicate
    def click_duplicate_icon(self):
        self.do_click(self.DUPLICATE_ICON)


    def get_page(self, index):
        pages = self.driver.find_elements(*self.PAGE)
        return pages[index-1]
    
    def is_page_on_list_page_display(self, index):
        try:
            page = self.get_page(index)
            return True
        except Exception:
            return False
    
    def select_page_in_page_list(self, index):
        page = self.get_page(index)
        page.click()    
        
    def delete_page_in_list_page(self, index):
        page = self.get_page(index)
        page.find_element(*self.DELETE_ICON).click()
        

    def get_page_in_tag_bar(self, index):
        pages = self.driver.find_elements(*self.PAGE_IN_TAG_BAR)
        return pages[index-1]
    
    def click_duplicate_icon_on_tab_bar(self, index):
        page = self.get_page_in_tag_bar(index)
        self.hover(page)
        icon = page.find_element(*self.DUPLICATE_ICON_ON_TAB_BAR)
        icon.click()

    
    def select_page_in_tag_bar(self, index):
        page = self.get_page_in_tag_bar(index)
        page.click()

    def delete_page_on_tag_bar(self, index):
        page = self.get_page_in_tag_bar(index)
        menu_page = page.find_element(By.CSS_SELECTOR, "#menu-page-1") 
        menu_page.click()
        delete_button = page.find_element(*self.DELETE_ICON_ON_TAG_BAR)
        delete_button.click()
        time.sleep(5)

    def is_page_on_tab_bar_display(self, index):
        try:
            self.get_page_in_tag_bar(index)
            return True
        except Exception:
            return False
    
    def is_page_on_tab_bar_selected(self, index):
        try:
            page = self.get_page_in_tag_bar(index)
            page.find_element(By.CSS_SELECTOR, '.menu-page[style="height: 174px; outline: rgb(53, 175, 255) solid 2px; cursor: pointer; position: relative;"]')
            return True
        except Exception:
            return False
        
    def close_template_menu(self):
        self.do_click(self.CLOSE_TEMPLATE_MENU)

    def hover_on_template_tab(self):
        template_tab = self.driver.find_element(*self.TEMPLATE_TAB)
        self.hover(template_tab)

    def click_template_tab(self):
        self.do_click(self.TEMPLATE_TAB)

    def is_template_tab_menu_display(self):
        return self.is_display(self.TEMPLATE_MENU)
    
    def is_tutorial_popup_display(self):
        return self.is_display(self.TUTORIAL_POPUP)
    
    def search_template(self, text):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys(text)

        self.do_click(self.SEARCH_BUTTON)

    def close_search_result(self):
        self.do_click(self.CLOSE_SEARCH)

    def edit_search_text(self, text):
        search_bar = self.driver.find_element(*self.SEARCH_BAR_2)
        search_bar.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        search_bar.send_keys(text)
        time.sleep(3)
        self.do_click(self.SEARCH_BUTTON_2)

    def is_text_no_result(self):
        return self.is_display(self.TEXT_NO_RESULT)
    
    def is_search_exactly_template(self, index):
        return self.is_display(self.TEMPLATE_FOR_SEARCH[index])
    
    def is_next_arrow_display(self):
        return self.is_display(self.NEXT_ARROW_BTN)
    
    def is_prev_arrow_display(self):
        return self.is_display(self.PREV_ARROW_BTN)
    
    def is_list_tag_display(self):
        return self.is_display(self.LIST_TAG)
    
    def click_next_arrow(self):
        return self.do_click(self.NEXT_ARROW_BTN)
    


    
    
