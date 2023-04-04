import time
import pytest
from testcases.test_base import BaseTest
from pages.GameInput import GameInputWorksheet
from Config.config import TestData
from Utilities.customLog import LogGen


class TestInputGame(BaseTest):
    logger = LogGen.loggen()

    def test_score_with_playing(self):
        self.logger.info("************* Test_001 ***************")
        #   Step1
        test_passed_status = True
        try:
            self.page = GameInputWorksheet(self.driver)
            flag = self.page.is_page_loaded()
            assert flag
            if flag:
                self.logger.info("********** Open worksheet  ********")
        except AssertionError as e:
            self.logger.error("******* Cannot open worksheet *******")
            test_passed_status = False
        #   Step2. Check input value
        try:
            self.page.fill_input()
            self.logger.info("********* Fill input ***********")
        except Exception as e:
            self.logger.error(e)
            self.logger.error("********** Cannot Input ************")
            test_passed_status = False


        #   Step3. Check Grade
        try:
            self.page.click_submit()
            self.logger.info("********* Submit ********")
            actual_location = self.page.get_position_of_grade()
            assert self.page.is_correct_location(actual_location, TestData.GRADE_LOCATION)

        except AssertionError as e:
            test_passed_status = False
            self.logger.error("***** Grade location not correct ******")


        #     Step4. Check grade format
        try:
            actual_grade_color = self.page.get_grade_color()
            if actual_grade_color == TestData.GRADE_COLOR:
                assert True
        except AssertionError as e:
            test_passed_status = False
            self.logger.error("******** Grade format not match *******")

        try:
            actual_grade_value = self.page.get_grade_value()
            assert actual_grade_value == 3
        except AssertionError as e:
            test_passed_status = False
            self.logger.error("******* Grade value wrong *******")
            self.logger.info(f"It showed {actual_grade_value}/10")

        if not test_passed_status:
            pytest.fail("Test Failed")
        else:
            self.logger.info("********* Test passed ********")

    # Test 007
    def test_score_without_playing(self):

        #   Step1: Open worksheet
        test_passed_status = True
        try:
            self.logger.info("****** Test 007 ******")
            self.page = GameInputWorksheet(self.driver)
            assert self.page.is_page_loaded()
            self.logger.info("*********** OpenWorksheet Successful **********")
        except AssertionError as e:
            self.logger.error("********* Cant open work sheet *************")
            test_passed_status = False

        #   Step2: Score in top right
        try:
            self.page.click_submit()
            self.logger.info("********** Submit ***********")
        except Exception as e:
            test_passed_status = False

        try:
            actual_location = self.page.get_position_of_grade()
            assert self.page.is_correct_location(actual_location, TestData.GRADE_LOCATION)
        except AssertionError as e:
            test_passed_status = False
            self.logger.error("********* Grade location not correct *********")
            self.logger.info(f'{actual_location}')
        #     Step3. Check grade format
        try:
            actual_grade_color = self.page.get_grade_color()
            assert actual_grade_color == TestData.GRADE_COLOR
        except AssertionError as e:
            test_passed_status = False
            self.logger.error("*********** Grade format not match *******")

        try:
            actual_grade_value = self.page.get_grade_value()
            assert actual_grade_value == 0
        except AssertionError as e:
            test_passed_status = False
            self.logger.error("*********** Grade value wrong *******")
            self.logger.info(f"It showed {actual_grade_value}/10")
        if not test_passed_status:
            pytest.fail("Test failed")
        else:
            self.logger.info("******** Test passed ***********")


    # 3
    def test_play_game(self):
        test_passed_status = True
        try:
            self.logger.info("****** Test 008 ******")
            self.page = GameInputWorksheet(self.driver)
            assert self.page.is_page_loaded()
            self.logger.info("*********** OpenWorksheet Successful **********")
        except AssertionError as e:
            self.logger.error("********* Cant open work sheet *************")
            test_passed_status = False

        try:
            self.page.fill_input()
        except Exception as e:
            self.logger.error(e)
            self.logger.error("********* Cant input value *************")
            test_passed_status = False

        try:
            self.page.clear_input()
            self.logger.info("********** Cleared all input ************")
        except Exception as e:
            self.logger.info(e)
            self.logger.error("********* Cant clear inputted value *************")
            test_passed_status = False
            self.logger.info("******** Test pass *************")
        if not test_passed_status:
            pytest.fail("Test failed")
        else:
            self.logger.info("************* Test pass ***********")

    # 4. Show answer
    def test_show_answer(self):
        self.logger.info("****** Test 009 *******")
        test_passed_status = True
        try:
            self.page = GameInputWorksheet(self.driver)
            if self.page.is_page_loaded():
                self.logger.info("******** Open worksheet  *******")
            else:
                assert self.page.is_page_loaded()
        except Exception as e:
            self.logger.info(e)
            self.logger.error("*********Cant open work sheet*********")
            test_passed_status = False

        try:
            self.page.click_submit()
            self.logger.info("********* Click submit *********")
            self.show_answer_button = self.page.get_show_answer_button()
            if bool(self.show_answer_button):
                assert True
        except Exception as e:
            self.logger.info(e)
            self.logger.error("**** Show answer button not clickable ****")
            test_passed_status = False

        try:
            self.page.click_show_answer_button()
            assert self.page.get_show_answer_button().text == "Hide answers"
            self.logger.info("******** Show answer *********** ")
        except AssertionError as e:
            self.logger.info(e)
            self.logger.error("**** Show answers not change to Hide answers *******")
            test_passed_status = False

        try:
            assert self.page.get_answers() == TestData.INPUT_ANSWER
        except AssertionError as e:
            self.logger.error("********* Answers not match *************")
            test_passed_status = False
        if not test_passed_status:
            pytest.fail("Test failed")
        else:
            self.logger.info("*********** Test passed ************")

    # Hide answer
    def test_hide_answer(self):
        self.logger.info("****** Test 010 ******")
        test_passed_status = True
        try:
            self.page = GameInputWorksheet(self.driver)
            if self.page.is_page_loaded():
                self.logger.info("******** OpenWorksheet Successful **********")
            else:
                assert self.page.is_page_loaded()
        except AssertionError as e:
            self.logger.error("Cant open worksheet")
            test_passed_status = False

        try:
            self.page.click_submit()
            self.logger.info("********* Submitted ***************")
            assert bool(self.page.get_show_answer_button())

        except AssertionError:
            self.logger.error("******* Show answer button not visible *******")
            test_passed_status = False

        try:
            self.page.click_show_answer_button()
            assert self.page.get_show_answer_button().text == "Hide answers"
        except AssertionError:
            self.logger.error("**** Show answers not change to Hide answers ********")

        try:
            self.page.click_show_answer_button()
            self.logger.info("******** Hide answers ********")
            assert self.page.get_show_answer_button().text == "Show answers"
        except AssertionError:
            self.logger.error("********* Hide answers not change to Show answers *************")
            test_passed_status = False

        try:
            answers = self.page.get_answers()
            str = "".join(answers)
            assert str == ""
        except AssertionError as e:
            self.logger.error(e)
            test_passed_status = False

        if not test_passed_status:
            pytest.fail("Test failed")
        else:
            self.logger.info("*********** Test passed ************")

    def test_try_again(self):
        test_passed_status = True
        try:
            self.page = GameInputWorksheet(self.driver)
            if self.page.is_page_loaded():
                self.logger.info("*********** Open worksheet  **********")
            else:
                assert self.page.is_page_loaded()
        except Exception as e:
            self.logger.error("***************** Cant open worksheet *************")
            test_passed_status = False

        try:
            self.page.click_submit()
            self.logger.info("********* Submit ************")
            try_again_button = self.page.get_try_again_button()
            assert bool(try_again_button)
        except AssertionError:
            self.logger.error("****** Submit button not change to try again ***")
            test_passed_status = False

        try:
            input_boxes = self.page.get_input_boxes()
            for box in input_boxes:
                assert not box.is_enabled()
        except AssertionError:
            self.logger.error("********* Still able to fill the input *********")
            test_passed_status = False

        try:
            self.page.escape()
            self.page.click_try_again_button()
            self.logger.info("****** Click try again button ********")
            submit_button = self.page.get_submit_button()
            assert bool(submit_button)
        except AssertionError:
            self.logger.error("***** Try again button not change to submit ******")
            test_passed_status = False

        try:
            input_boxes = self.page.get_input_boxes()
            for box in input_boxes:
                assert box.is_enabled()
        except AssertionError:
            self.logger.error("********* Not able to fill the input *********")
            test_passed_status = False

        if not test_passed_status:
            pytest.fail("Test failed")
        else:
            self.logger.info("*********** Test passed ************")





























