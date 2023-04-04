import time

import pytest

from pages.GameConnect import GameConnect
from testcases.test_base import BaseTest
from pages.GameInput import GameInputWorksheet
from Config.config import TestData
from Utilities.customLog import LogGen


class TestConnectGame(BaseTest):
    logger = LogGen.loggen()

    def test_score_with_connect(self):
        pytest.skip()
        # test_passed_flag = True
        # try:
        #     self.play_page = GameConnect(self.driver)
        #     if self.play_page.is_page_loaded():
        #         self.logger.info("*********** OpenWorksheet Successful **********")
        #     else:
        #         assert self.play_page.is_page_loaded()
        # except Exception as e:
        #     self.logger.error("Cant open worksheet")
        #     test_passed_flag = False
        #
        # try:
        #     self.play_page.connect()
        #     time.sleep(5)
        #     self.logger.info("****Oke*****")
        # except Exception as e:
        #     self.logger.error(e)
        #     self.logger.error("******* cannot connect **********")
        #     test_passed_flag = False
        #
        # if not test_passed_flag:
        #     pytest.fail("**Test failed**")