import pytest
from Config.config import TestData
from testcases.test_base import BaseTest
from pages.GameInput import GameInputWorksheet
from pages.PreviewPage import PreviewPage
from pages.CreateWorksheetPage import CreateWorksheetPage
from Utilities.customLog import LogGen


class TestGeneral(BaseTest):
    logger = LogGen.loggen()

    # Test 003
    def test_submit_button_location(self):
        self.logger.info("******* Test 003 ******")
        test_passed_flag = True
        try:
            self.play_page = GameInputWorksheet(self.driver)
            assert self.play_page.is_page_loaded()
            self.logger.info("****** Open Input Game ******")
        except Exception as e:
            self.logger.error("****** Cant open worksheet ******")
            test_passed_flag = False

        try:
            submit_btn_location = self.play_page.get_submit_button_location()
            assert self.play_page.is_correct_location(submit_btn_location, TestData.SUBMIT_BUTTON_LOCATION)

        except AssertionError:
            self.logger.error("************ Submit button location not match *************")
            self.logger.info(submit_btn_location)
            test_passed_flag = False

        try:
            self.play_page.click_submit()
            self.logger.info("****** Submit *******")
            try_again_button = self.play_page.get_try_again_button()
            assert bool(try_again_button)
        except AssertionError:
            self.logger.error("*********** Submit button not change to try again ********")
            test_passed_flag = False

        try:
            self.try_again_button_location = self.play_page.get_try_again_button_location()
            assert self.play_page.is_correct_location(self.try_again_button_location, TestData.TRY_AGAIN_BUTTON_LOCATION)
        except AssertionError:
            self.logger.error("************ Try again button location not match *************")
            self.logger.info(self.try_again_button_location)
            test_passed_flag = False

        try:
            self.play_page.escape()
            self.play_page.click_three_dots_button()
            self.try_again_btn_drop_down_location = self.play_page.get_try_again_button_location()
            assert self.play_page.is_correct_location(
                self.try_again_btn_drop_down_location, TestData.SUBMIT_BUTTON_LOCATION_DROP_DOWN
            )
        except AssertionError:
            self.logger.error(
                "************ Try again button location after click three dot btn not match *************")
            self.logger.info(self.try_again_btn_drop_down_location)
            test_passed_flag = False

        if not test_passed_flag:
            pytest.fail("************** Test failed ************")
        else:
            self.logger.info("******** Test passed *********")

    # 5
    def test_interactive_box_location(self):
        test_passed_flag = True
        try:
            self.logger.info("****** Test 005 ******")
            self.preview_page = PreviewPage(self.driver)
            self.preview_page.open_browser()
            assert self.preview_page.is_page_loaded()
            self.logger.info("*********** Open PreviewPage **********")
        except AssertionError as e:
            self.logger.error("************** Cant open worksheet ****************")
            test_passed_flag = False

        try:
            self.interactive_box_locations = self.preview_page.get_interactive_box_location()
            for i in range(len(self.interactive_box_locations)):
                assert self.preview_page.is_correct_location(
                    self.interactive_box_locations[i], TestData.INTERACTIVE_BOXES_LOCATION_PREVIEW_PAGE[i]
                )
        except AssertionError:
            self.logger.error("************ Interactive box location not match *************")
            self.logger.info(self.interactive_box_location)
            test_passed_flag = False

        try:
            play_page = self.preview_page.click_play_now_button()
            self.logger.info("****** Redirect to play page *******")
        except Exception as e:
            self.logger.error(e)
            self.logger.error("************ Cannot open play page *************")
            test_passed_flag = False

        try:
            interactive_boxes_location_play_page = play_page.get_interactive_box_location()
            for i in range(len(interactive_boxes_location_play_page)):
                assert play_page.is_correct_location(
                    interactive_boxes_location_play_page[i], TestData.INTERACTIVE_BOXES_LOCATION_PLAY_PAGE[i]
                )
        except AssertionError:
            self.logger.error("***** Interactive box location in play page not match *****")
            self.logger.info(interactive_boxes_location_play_page)
            test_passed_flag = False

        if not test_passed_flag:
            pytest.fail("************** Test failed ************")
        else:
            self.logger.info("****** Test passed ******")
