import sys
import os

from selenium import webdriver


#  Webdriver Factory holds all the settings and configurations
#  ... required for the browser

class WebdriverFactory:

    def get_driver(self, browser):
        try:
            print(browser)
            if browser.lower() == "firefox":
                driver = webdriver.Firefox(executable_path="C:\\Users\\Dpkpc\\PycharmProjects\\DNBAssignment Pytest\\Driver\\geckodriver.exe")
              #driver = webdriver.Firefox(
              #executable_path=os.path.realpath(__file__)+"\\Driver\\geckodriver.exe")
            elif browser.lower() == "chrome":
                print("We are here")
                driver = webdriver.Chrome(
                    executable_path="C:\\Users\\Dpkpc\\PycharmProjects\\DNBAssignment Pytest\\Driver\\chromedriver.exe")
            else:
                raise Exception("Invalid Browser value provided")
            print(driver)
            return driver
        except:
            raise Exception(str(sys.exc_info()))
