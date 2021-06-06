import pytest
from Pages import ExcelFunctions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Pages.Locators import Locators
from selenium import webdriver
from Utils.WebdriverFactory import WebdriverFactory
import allure
from Pages.LoginPage import LoginPage
import pytest_failed_screenshot
import sys
from Pages import CommonData


################## Documentation#########################
# Verify the invalid login attempts pushed through an input sheet uploaded
# ... at the Driver Folder

class Test_InvalidLogin():

    # Runs through the excel sheet and attempts login with credentials
    @allure.description("Test Run Through Invalid Inputs")
    @allure.step
    def test_RunThroughInvalidInputs(self):
        driver = None
        try:
            driver = WebdriverFactory().get_driver(CommonData.BROWSER)
            driver.get(CommonData.BASEURL)
            lp = LoginPage(driver)
            lp.excel_iteration()
        except:
            if driver:
                allure.attach(driver.get_screenshot_as_png(),
                              name="Screenshot of Error",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(sys.exc_info()), 'Error Trace', allure.attachment_type.TEXT)
            raise Exception(str(sys.exc_info()))

        finally:
            if driver:
                driver.close()

