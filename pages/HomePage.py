from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Config.config import TestData
from pages.BasePage import BasePage
from pages.CreateWorksheetPage import CreateWorksheetPage
from pages.PreviewPage import PreviewPage


class HomePage(BasePage):
    USER = (By.CSS_SELECTOR, ".user")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.split-user-header > div > div > div > p:nth-child(3)")
    INPUT = (By.CSS_SELECTOR, "#outlined-basic")
    LOGIN_AND_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#content-step > div.auth > div > button")

    CREATE_WORKSHEET_BUTTON = (By.CSS_SELECTOR, ".cta-header.create-worksheet-header")
    GET_STARTED_BTN = (By.CSS_SELECTOR, ".btn-get-started")
    FIRST_WORKSHEET = (By.CSS_SELECTOR, "div.data-grid-item.data-worksheet.user")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.HOME_PAGE_URL)

    def login(self):
        drop_down = self.driver.find_element(*self.USER)
        drop_down.click()
        login = self.driver.find_element(*self.LOGIN_BUTTON)
        login.click()

        input_box = self.driver.find_element(*self.INPUT)
        input_box.send_keys(TestData.EMAIL_USERNAME)

        login_and_download_button = self.driver.find_element(*self.LOGIN_AND_DOWNLOAD_BUTTON)
        login_and_download_button.click()

        self.escape()

    def get_started(self):
        create_ws_button = self.driver.find_element(*self.CREATE_WORKSHEET_BUTTON)
        create_ws_button.click()

        get_started_btn = self.driver.find_element(*self.GET_STARTED_BTN)
        get_started_btn.click()

        return CreateWorksheetPage(self.driver)

    def select_worksheet(self):
        class AnyPreviewPage(PreviewPage):
            def __init__(self, driver):
                super().__init__(driver)

            def open_ws(self):
                pass
        ws = self.driver.find_element(*self.FIRST_WORKSHEET)
        ws.click()
        return AnyPreviewPage(self.driver)










