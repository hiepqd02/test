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


class TestCreateWsTemplate(BaseTest):
    logger = LogGen.loggen()

    #123: UI Skipp 

    # 004
    def test_close_template_menu(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        

        create_page.close_template_menu()

        assert not create_page.is_template_tab_menu_display()

        create_page.hover_on_template_tab()

        assert create_page.is_tutorial_popup_display()

        create_page.click_template_tab()
  
        assert create_page.is_template_tab_menu_display()
    # 006
    def test_search_not_existed_template(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.search_template("kjdhakj")

        assert not create_page.is_text_no_result()

    # 007
    def test_search_exactly_template(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.search_template("Pastel Fun Activity Calendar Worksheet")
        
        assert create_page.is_search_exactly_template(0)

    # 009
    def test_search_upper_case(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.search_template("Pastel Fun Activity Calendar Worksheet")
        
        assert create_page.is_search_exactly_template(0)

        create_page.close_search_result()

        create_page.search_template("PASTEL FUN ACTIVITY CALENDAR WORKSHEET")
        
        assert create_page.is_search_exactly_template(0)
        
    # 011
    def test_edit_search_text(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.search_template("Pastel Fun Activity Calendar Worksheet")
        
        assert create_page.is_search_exactly_template(0)
        time.sleep(5)

        create_page.search_template("Under the Sea Word Search")
        
        assert create_page.is_search_exactly_template(1)

    # 012
    def test_delete_search_text(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()

        create_page.search_template("Pastel Fun Activity Calendar Worksheet")
        
        assert create_page.is_search_exactly_template(0)
        time.sleep(3)
        create_page.close_search_result()   
        time.sleep(3)

        assert not create_page.is_search_exactly_template(0)

    # 013
    
    def test_tag_bar_search_list(self):

        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()


        assert create_page.is_list_tag_display()

        assert create_page.is_next_arrow_display()

        create_page.click_next_arrow()

        assert create_page.is_prev_arrow_display()

        while 1:
            if not create_page.is_next_arrow_display():
                break
            create_page.click_next_arrow()
            time.sleep(1)
        
        assert not create_page.is_next_arrow_display()













