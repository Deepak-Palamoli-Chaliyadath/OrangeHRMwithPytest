from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
import HTMLTestRunner
# import sys
import time
from Utils.WebdriverFactory import WebdriverFactory
import allure
import base64
import pytest_failed_screenshot
from Pages import CommonData

# sys.path.append("C://Users/Dpkpc/PycharmProjects/DNBAssignment Pytest")
import pytest


################## Documentation#########################
# Verify the Valid login on Orange HRM website
# ... and prints the name of the user in allure reports

class Test_Login():

    def test_Login(self):
        driver = WebdriverFactory().get_driver(CommonData.BROWSER)
        driver.get(CommonData.BASEURL)
        lp = LoginPage(driver)
        lp.LoginMethod()
        time.sleep(3)
        db = DashboardPage(driver)
        txt_first_name = db.captureWelcomeName()
        allure.attach(str(txt_first_name), 'Name of User', allure.attachment_type.TEXT)
        allure.attach(driver.get_screenshot_as_png(),
                      name="Name of User",
                      attachment_type=allure.attachment_type.PNG)
        db.clickWelcome()
        db.clickLogout()
        driver.close()
