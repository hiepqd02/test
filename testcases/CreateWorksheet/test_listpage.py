import time
from math import isclose
import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from pages.CreateWorksheetPage import CreateWorksheetPage
from pages.HomePage import HomePage
from pages.GameInput import GameInputWorksheet
from pages.PreviewPage import PreviewPage
from testcases.test_base import BaseTest
from Utilities.customLog import LogGen


class TestCreateWs(BaseTest):
    logger = LogGen.loggen()

    def test_open_create_page_from_play(self):
        self.logger.info("****** Test 002 *********")
        play_page = GameInputWorksheet(self.driver)
        self.logger.info("****** Play Page ******")
        play_page.click_customize_icon()
        create_page = play_page.click_customize_button()
        self.logger.info("*****Create Page *****")
        self.logger.info("***** Test passed ******")

    def test_open_create_page_from_preview(self):
        self.logger.info("****** Test 003 *********")
        preview_page = PreviewPage(self.driver)
        preview_page.open_browser()
        self.logger.info("****** Preview Page ******")
        create_page = preview_page.click_customize_button()
        self.logger.info("*****Create Page *****")
        self.logger.info("***** Test passed ******")

    def test_save_worksheet_after_upload(self):
        try:
            self.home_page = HomePage(self.driver)
            self.home_page.login()
            assert self.home_page.is_page_loaded()
            self.logger.info("********* Home page ***********")
        except Exception as e:
            self.logger.error(f'{e}')
            pytest.fail("******** Cannot open Home Page *********")

        self.create_ws_page = self.home_page.get_started()
        self.logger.info("******** Create Page **********")
        self.create_ws_page.switchTab(1)
        self.create_ws_page.upload_file()
        self.logger.info("********* File uploaded ********")
        self.create_ws_page.click_red_save_button()

        try:
            assert bool(self.create_ws_page.get_save_pop_up())
        except Exception:
            pytest.fail("******** Save popup not found *********")

        self.create_ws_page.input_ws_name()
        self.logger.info("******* Fill save pop up **********")

        self.create_ws_page.click_blue_save_button()
        try:
            time.sleep(5)
            self.create_ws_page.get_shared_popup()
        except Exception:
            self.logger.error("********** Shared popup not found *******")
            pytest.fail("******** Shared popup not found *********")
        self.logger.info("******* Test passed *******")

    def test_save_ws_template(self):
        home_page = HomePage(self.driver)
        self.logger.info("****** Homepage ********")
        home_page.login()
        self.logger.info("******** Login **********")

        self.create_ws_page = home_page.get_started()
        self.logger.info("*******  Create Ws Page **********")
        self.create_ws_page.switchTab(1)

        self.create_ws_page.pick_a_template()
        self.logger.info("****** Pick a template *******")

        self.create_ws_page.click_red_save_button()
        self.logger.info("********** Save ********")
        ##
        try:
            assert bool(self.create_ws_page.get_save_pop_up())
        except Exception:
            pytest.fail("******** Save pop up not found *********")

        self.create_ws_page.input_ws_name()
        self.logger.info("******* Fill pop up ********")

        self.create_ws_page.click_blue_save_button()
        self.logger.info("******* Save ******")
        # Test
        try:
            self.create_ws_page.get_shared_popup()
        except Exception:
            pytest.fail("******** Shared popup not found *********")
        self.logger.info("******* Test passed *******")

    def test_save_blank_ws(self):
        home_page = HomePage(self.driver)
        self.logger.info("******* HomePage *********")
        home_page.login()
        self.logger.info("******* Login ********")

        self.create_ws_page = home_page.get_started()
        self.logger.info("******* CreatePage ********")
        self.create_ws_page.switchTab(1)

        self.create_ws_page.click_red_save_button()
        self.logger.info("******** Save ********")
        try:
            assert bool(self.create_ws_page.get_the_message_bar())
        except Exception:
            self.logger.error("Upload or select template Message ")
            pytest.fail("******** Test failed *******")
        self.logger.info("*******Test passed *******")

    def test_undo_redo(self):
        self.logger.info("********** Test 004, 005 *********")
        home_page = HomePage(self.driver)
        self.logger.info("********** Home Page*********")
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.pick_a_template()
        self.logger.info("********** Pick a template *********")

        try:
            assert self.create_ws_page.is_template_display()
        except AssertionError:
            self.logger.error("******** Page not display template ******")
            pytest.fail()

        # self.create_ws_page.undo_redo_btn("hover", "undo")
        self.create_ws_page.undo_redo_btn("click", "undo")
        self.logger.info("********** Undo *********")

        try:
            assert not self.create_ws_page.is_template_display()
        except AssertionError:
            self.logger.error("****** Page not return to blank page *******")
            pytest.fail()

        # self.create_ws_page.undo_redo_btn("hover", "redo")
        self.create_ws_page.undo_redo_btn("click", "redo")
        self.logger.info("********** Redo *********")

        try:
            assert self.create_ws_page.is_template_display()
        except AssertionError:
            self.logger.error("******** Page not display template ******")
            pytest.fail()

        self.logger.info("***** Test passed *******")

    def test_zoom(self):
        self.logger.info("****** Test 006 *****")
        home_page = HomePage(self.driver)
        self.logger.info("********* Home Page *****")
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)
        self.logger.info("******* Create Page ******")

        self.create_ws_page.change_ws_size(45)
        self.logger.info("****** Zoom out *******")
        position_45 = self.create_ws_page.get_page_position()
        try:
            assert isclose(
                position_45['x'], TestData.PAGE_POSITION[0]['x'], abs_tol=1
            ) and isclose(
                position_45['y'], TestData.PAGE_POSITION[0]['y'], abs_tol=1
            )
        except AssertionError:
            pytest.fail()
            self.logger.error("***** Zoom out failed *****")

        self.create_ws_page.change_ws_size(200)
        self.logger.info("******* Zoom in *******")
        position_200 = self.create_ws_page.get_page_position()
        try:
            assert isclose(
                position_200['x'], TestData.PAGE_POSITION[1]['x'], abs_tol=1
            ) and isclose(
                position_200['y'], TestData.PAGE_POSITION[1]['y'], abs_tol=1
            )
            self.logger.info("******* Test passed ******")
        except AssertionError:
            pytest.fail()
            self.logger.error("****** Zoom in failed ******")

    def test_feed_back_pop_up_1(self):
        self.logger.info("****** Test 008 ******")
        pytest.skip()
        home_page = HomePage(self.driver)
        # home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        time.sleep(15)

    def test_feed_back_pop_up_2(self):
        self.logger.info("****** Test 009 ******")
        pytest.skip()
        home_page = HomePage(self.driver)
        # home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)
        time.sleep(15)

    def test_add_page_with_button(self):
        self.logger.info("***** Test 015 *****")
        home_page = HomePage(self.driver)
        self.logger.info("******* Home Page *******")
        preview_page = home_page.select_worksheet()
        create_ws_page = preview_page.click_customize_button()
        create_ws_page.switchTab(1)
        time.sleep(5)
        self.logger.info("****** Create Page ******")

        create_ws_page.add_page_with_button()
        time.sleep(10)
        self.logger.info("********* Add Page ********")
        try:
            current_page = create_ws_page.get_page_position()['top']
            assert isclose(current_page, 30, abs_tol=1)
        except AssertionError:
            self.logger.info(create_ws_page.get_page_position())
            pytest.fail("******* Scroll to page failed *****")
        self.logger.info("******* Test passed *****")

    def test_add_page_with_icon(self):
        self.logger.info("****** Test 016 *****")
        home_page = HomePage(self.driver)
        self.logger.info("******* Home Page *****")
        preview_page = home_page.select_worksheet()
        create_ws_page = preview_page.click_customize_button()
        create_ws_page.switchTab(1)
        self.logger.info("**** Create Page *****")
        time.sleep(5)
        create_ws_page.add_page_with_icon()
        time.sleep(10)
        try:
            current_page = create_ws_page.get_page_position()['top']
            assert isclose(current_page, 30, abs_tol=1)
        except AssertionError:
            self.logger.info(create_ws_page.get_page_position())
            pytest.fail("******* Scroll to page failed *****")
        self.logger.info("******* Test passed *****")
    #      Test 018

    def test_duplicate_page(self):
        pytest.skip()

    #   Test 019
    def test_move_up_down(self):
        pytest.skip()

    #     Test 020
    def test_scroll_to_top(self):
        self.logger.info("******** Test 020 **********")
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        self.logger.info("********* Create Page *******")

        create_page.scroll_to_bottom()
        self.logger.info("********* Scroll to bottom *****")

        try:
            assert bool(create_page.is_up_button_display())
        except AssertionError:
            self.logger.error("***** Up-arrow button not display***")
            pytest.fail()

        create_page.click_scroll_to_top_button()
        self.logger.info("******** Click up-arrow button ******")
        time.sleep(2)
        try:
            assert not bool(create_page.is_up_button_display())
        except AssertionError:
            self.logger.error("****** Up-arrow button still display ****")
            pytest.fail()
        self.logger.info("**** Test Passed *****")

    def test_tag_bar_when_add_new_page(self):
        # pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        
        create_page.click_on_tag_bar_icon()
        time.sleep(5)

        create_page.add_page_with_button()
        time.sleep(5)

        create_page.add_page_with_icon()
        time.sleep(5)


    def test_tag_bar_when_duplicate(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        

        create_page.click_on_tag_bar_icon()
        time.sleep(5)

        create_page.click_duplicate_icon()
        time.sleep(5)
        
    def test_tag_bar_when_edit(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        
        create_page.click_on_tag_bar_icon()
        time.sleep(5)

        create_page.pick_a_template()
        time.sleep(5)

        create_page.add_page_with_icon()
        time.sleep(5)

        create_page.pick_a_template()
        time.sleep(5)

    # Testcase 25
    def test_tag_bar_when_delete(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        

        create_page.click_on_tag_bar_icon()
        for i in range(3):
            create_page.add_page_with_button()
            time.sleep(3)

        create_page.delete_page_in_list_page(1)

        time.sleep(3)

        create_page.delete_page_in_list_page(2)

        time.sleep(3)

    def test_select_page_on_tag_bar(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()


        for i in range(4):
            create_page.add_page_with_button()
            time.sleep(1)        
        
        create_page.click_on_tag_bar_icon()

        create_page.select_page_in_page_list(2)
        time.sleep(2)

        create_page.select_page_in_tag_bar(3)
        time.sleep(2)
        
        create_page.scroll_to_bottom()
        time.sleep(2)

        create_page.select_page_in_page_list(5)
        time.sleep(2)
    
    def test_delete_page_list_page(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()


        for i in range(4):
            create_page.add_page_with_button() 
            time.sleep(1)        
        
        create_page.click_on_tag_bar_icon()

        create_page.delete_page_in_list_page(1)
        time.sleep(2)

        create_page.delete_page_in_list_page(2)
        time.sleep(2)

    def test_delete_page_on_tag_bar(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.click_on_tag_bar_icon()

        for i in range(4):
            create_page.add_page_with_button() 
            time.sleep(1)        
        


        create_page.delete_page_on_tag_bar(3)

        

    def test_page(self):
        pytest.skip()
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        locator = (By.CSS_SELECTOR, "#app > div:nth-child(1) > div > div.header-create-ws")
        self.logger.info(create_page.get_element_location(locator))