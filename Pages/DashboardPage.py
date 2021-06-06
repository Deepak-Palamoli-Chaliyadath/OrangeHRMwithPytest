from selenium import webdriver
from Pages.Locators import Locators
from selenium.webdriver.common.by import By
# Dashboard Page Class holds all the method definitions of
#  the actions which can be performed on the dashboard page.
class DashboardPage():

    def __init__(self, drv):
        self.driver = drv

    # Captures the Name which comes along with Welcome on Top Right of Dashboard page
    def captureWelcomeName(self):
        txtWelcome = self.driver.find_element(By.ID, Locators.db_lbl_Welcome_id)
        arrtxtWelcome = txtWelcome.text.split(sep=" ")
        return arrtxtWelcome[1]

    # Clicks on Welcome on Top Right of Dashboard page before Logout
    def clickWelcome(self):
        self.driver.find_element(By.ID, Locators.db_lbl_Welcome_id).click()

    # Clicks on Logout on Top Right of Dashboard page after Welcome is clicked
    def clickLogout(self):
        self.driver.find_element(By.XPATH, Locators.db_lbl_Logout_xpath).click()