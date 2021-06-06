import time
from selenium import webdriver
from Pages.Locators import Locators
from selenium.webdriver.common.by import By
# My Info Page Class holds all the method definitions of
#  the actions which can be performed on the my info page.
class MyInfoPage():
    def __init__(self,drv):
        self.driver = drv

    # Clicks on the My info tab
    def clickMyInfoTab(self):
        self.driver.find_element(By.ID, Locators.mi_lbl_MyInfo_id).click()

    # Fetch the First name from the My info tab
    def fetchFirstName(self):
        self.driver.find_element(By.ID, Locators.mi_lbl_MyInfo_id).click()
        time.sleep(3)
        lbl_FirstName = self.driver.find_element(By.ID, Locators.mi_lbl_FirstName_id).get_attribute('value')
        return lbl_FirstName