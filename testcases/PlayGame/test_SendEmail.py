import pytest
from testcases.test_base import BaseTest
from pages.GameInput import GameInputWorksheet
from Config.config import TestData
from Utilities.customLog import LogGen


class TestSendEmail(BaseTest):
    logger = LogGen.loggen()

    def test_send_without_fill_input(self):
        pytest.skip()

    def test_send_email(self):
        pytest.skip()
        test_passed_status = True
        try:
            self.page = GameInputWorksheet(self.driver)
            if self.page.is_page_loaded():
                self.logger.info("*********** Open worksheet **********")
            else:
                assert self.page.is_page_loaded()
        except AssertionError as e:
            self.logger.error("***************** Cant open worksheet *************")
            test_passed_status = False

        try:
            self.page.click_submit()
            send_email_button = self.page.get_send_email_button()
            assert bool(send_email_button)
        except AssertionError as e:
            self.logger.error("************ Send email to teacher button not visible ************")
            test_passed_status = False

        try:
            self.page.click_send_email_button()
            send_email_popup = self.page.get_send_email_popup()
            assert bool(send_email_popup)
            self.logger.info("*********** Email popup *************")
        except AssertionError:
            self.logger.error("********** No send email popup ***********")
            test_passed_status = False
        except Exception as e:
            self.logger.error(e)

        try:
            self.page.fill_email_popup_info()
            self.logger.info("********* Filled ********")
            self.page.click_send_button()
            self.logger.info("******** Send ********")
            pop_up = self.page.get_alert_success_popup()
            assert bool(pop_up)
        except AssertionError:
            self.logger.error("*********** Pop-up not shown **************")
            test_passed_status = False
        except Exception as e:
            self.logger.error(e)
            test_passed_status = False
        if not test_passed_status:
            pytest.fail("Test failed")