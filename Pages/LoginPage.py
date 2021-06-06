import os

from selenium import webdriver
from Pages.Locators import Locators
from selenium.webdriver.common.by import By
from Pages import ExcelFunctions
import pytest_failed_screenshot


# Login Page Class holds all the method definitions of
#  the actions which can be performed on the login page.

class LoginPage():

    def __init__(self, drv):
        self.driver = drv

    # Captures the user name of the valid login from the label in login page
    def captureUserName(self):
        lbl_credentials = self.driver.find_element(By.XPATH, Locators.hp_lbl_Credentials_xpath)
        arrlbl_credentials = lbl_credentials.text.split(sep=" ")
        return arrlbl_credentials[3]

    # Captures the password of the valid login from the label in login page
    def capturePassword(self):
        lbl_credentials = self.driver.find_element(By.XPATH, Locators.hp_lbl_Credentials_xpath)
        arrlbl_credentials = lbl_credentials.text.split(sep=" ")
        return arrlbl_credentials[7]

    # Set the username provided as input in the username text box on Login page
    def setUsername(self, username):
        self.driver.find_element_by_id(Locators.hp_txt_username_id).send_keys(username)

    # Set the password provided as input in the password text box on Login page
    def setPassword(self, password):
        self.driver.find_element_by_id(Locators.hp_txt_password_id).send_keys(password)

    # Click on the login button
    def clickLogin(self):
        self.driver.find_element_by_id(Locators.hp_btn_Login_id).click()

    # Excel iteration of input data and login attempts using that data on Login page
    def excel_iteration(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        #path = 'C:\\Users\\Dpkpc\\PycharmProjects\\DNBAssignment Pytest\\Driver\\InputTestData.xlsx'
        path= ROOT_DIR + '\\Driver\\InputTestData.xlsx'
        int_rows = ExcelFunctions.getNumberOfRows(path, "InputTestData")
        int_cols = ExcelFunctions.getNumberOfColumns(path, "InputTestData")
        for iCount in range(2, int_rows + 1):
            txt_errormessage = "none"
            # All the input data are collected and stored in a variable
            txt_username = ExcelFunctions.readData(path, "InputTestData", iCount, 1) or ""
            txt_password = ExcelFunctions.readData(path, "InputTestData", iCount, 2) or ""
            txt_errormessage = ExcelFunctions.readData(path, "InputTestData", iCount, 3) or ""
            # The current browser are set with data collected from the above call
            self.LoginMethod(txt_username, txt_password)
            element = self.driver.find_element(By.ID, Locators.hp_lbl_ErrorMessage_id)
            # Verification of the Error message with the expected error message in Excel
            print(element.text + " " + txt_errormessage)
            assert element.text == txt_errormessage

    def LoginMethod(self, username, password):
        username = username or self.captureUserName()
        password = password or self.capturePassword()
        self.driver.find_element_by_id(Locators.hp_txt_username_id).send_keys(username)
        self.driver.find_element_by_id(Locators.hp_txt_password_id).send_keys(password)
        self.driver.find_element_by_id(Locators.hp_btn_Login_id).click()
