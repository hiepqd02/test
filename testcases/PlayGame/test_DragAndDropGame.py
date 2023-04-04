import time
import pytest
from Utilities.customLog import LogGen
from testcases.test_base import BaseTest
from pages.GameDragDrop import GameDragAndDrop


class TestDragAndDropGame(BaseTest):
    logger = LogGen.loggen()

    def test_score_with_play(self):
        pytest.skip()

        #   Step1
        test_passed_status = True
        try:
            self.play_page = GameDragAndDrop(self.driver)
            flag = self.play_page.is_page_loaded()
            assert flag
            if flag:
                self.logger.info("************* Open worksheet successfully ***********")
        except AssertionError as e:
            self.logger.error("********* Cannot open worksheet ********")
            test_passed_status = False

        try:
            self.play_page.drag_cube_shape()
            time.sleep(3)
            self.play_page.drag_cone_shape()
            time.sleep(3)
            # self.play_page.drag_to_location(source,620,900)
        except Exception as e:
            self.logger.error(e)
            test_passed_status = False

        if not test_passed_status:
            pytest.fail("Test Failed")
        #










