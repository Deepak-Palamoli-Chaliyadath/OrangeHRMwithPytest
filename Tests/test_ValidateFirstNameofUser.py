import allure
import pytest
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
from Pages.MyInfoPage import MyInfoPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Pages.Locators import Locators
from selenium import webdriver
import time
from Utils.WebdriverFactory import WebdriverFactory
import sys
from Pages import CommonData


################## Documentation############################
# Verify the Valid login on Orange HRM website and validates
# ... the name of the user in my info tab and welcome label

class Test_ValidateFirstNameofUser():

    def test_validate_user_from_myinfo(self):
        driver = None
        try:
            driver = WebdriverFactory().get_driver(CommonData.BROWSER)
            driver.get(CommonData.BASEURL)
            lp = LoginPage(driver)

            # Capture the username and password
            username = lp.captureUserName()
            password = lp.capturePassword()

            # Set the username and password and click login
            lp.setUsername(username)
            lp.setPassword(password)
            lp.clickLogin()
            time.sleep(5)

            # Capture the name on Welcome label
            db = DashboardPage(driver)
            txtFirstName = db.captureWelcomeName()
            print("Welcome screen name "+txtFirstName)

            # Capture the name on My info Page
            mi = MyInfoPage(driver)
            mi_txtFirstName = mi.fetchFirstName()
            print("My Info screen First name "+mi_txtFirstName)
            # Assert that both the names are same
            assert txtFirstName == mi_txtFirstName
            # Customer clicks on Welcome and logout
            db.clickWelcome()
            db.clickLogout()
            driver.close()

        except:
            if driver:
                allure.attach(driver.get_screenshot_as_png(),
                              name="Screenshot of Error",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(sys.exc_info()[0]), 'Error Trace', allure.attachment_type.TEXT)