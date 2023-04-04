import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class GameBase(BasePage):
    INPUT_BOX = (By.CSS_SELECTOR, ".fill-blank-input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    TRY_AGAIN_BUTTON = (By.CSS_SELECTOR, "#try-again-button")
    SHOW_ANSWER_BUTTON = (By.CSS_SELECTOR, "div.cta-action.show-answer")
    GRADE = (By.CSS_SELECTOR, ".content")
    THREE_DOTS_BUTTON = (By.CSS_SELECTOR, 'div.btn')

    # Pop-up
    SEND_EMAIL_BUTTON = (By.CSS_SELECTOR, '.send-result-for-teacher')
    SEND_EMAIL_POPUP = (By.CSS_SELECTOR, '.content-send-email-popup')
    POPUP_INPUT = (By.CSS_SELECTOR, 'input.MuiInputBase-input')
    SEND_BUTTON = (By.CSS_SELECTOR, '.button-send')
    ALERT_SUCCESS_POPUP = (By.CSS_SELECTOR, '.alert-success')
    BACK_BUTTON = (By.CSS_SELECTOR, '.back')

    # Submit/Try again
    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

    def click_submit(self):
        self.get_submit_button().click()

    def get_try_again_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TRY_AGAIN_BUTTON)
        )

    def click_try_again_button(self):
        self.get_try_again_button().click()

    # Grade
    def get_grade_element(self):
        return self.driver.find_element(*self.GRADE)

    def get_position_of_grade(self):
        return self.get_grade_element().location

    def get_grade_value(self):
        grade_value = self.get_grade_element().text[0]
        return int(grade_value)

    def get_grade_color(self):
        grade_color = self.get_grade_element().value_of_css_property('color')
        return grade_color

    # Show/Hide answers
    def get_show_answer_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SHOW_ANSWER_BUTTON)
        )

    def click_show_answer_button(self):
        self.do_lick(self.SHOW_ANSWER_BUTTON)

    def get_answers(self):
        list_answer = []
        answers = self.driver.find_elements(*self.INPUT_BOX)
        for answer in answers:
            list_answer.append(answer.get_attribute('value'))
        return list_answer

    # Send email to teacher
    def get_send_email_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEND_EMAIL_BUTTON)
        )

    def click_send_email_button(self):
        self.get_send_email_button().click()

    def get_send_email_popup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEND_EMAIL_POPUP)
        )

    def get_send_email_input(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'input')

    def fill_email_popup_info(self):
        time.sleep(2)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input.MuiInputBase-input.MuiInput-input.css-mnn31')
        # name = inputs[0]
        # name.send_keys("MyName")
        # level = inputs[1]
        # level.send_keys("MyLevel")
        # subject = inputs[2]
        # subject.send_keys("MySubject")
        # email = inputs[3]
        # email.send_keys("example@email.com")

    def click_send_button(self):
        self.do_lick(self.SEND_BUTTON)

    def get_alert_success_popup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.ALERT_SUCCESS_POPUP)
        )

    def get_submit_button_location(self):
        return self.get_location(self.SUBMIT_BUTTON)

    def get_try_again_button_location(self):
        return self.get_location(self.TRY_AGAIN_BUTTON)

    def click_three_dots_button(self):
        self.do_lick(self.THREE_DOTS_BUTTON)

    def click_back_arrow_button(self):
        self.do_lick(self.BACK_BUTTON)
