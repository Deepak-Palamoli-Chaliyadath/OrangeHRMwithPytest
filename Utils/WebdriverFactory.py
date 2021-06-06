import sys
import os

from selenium import webdriver


#  Webdriver Factory holds all the settings and configurations
#  ... required for the browser

class WebdriverFactory:

    def get_driver(self, browser):
        try:
            ROOT_DIR = os.path.abspath(os.curdir)
            if browser.lower() == "firefox":
                # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
                driver = webdriver.Firefox(executable_path=ROOT_DIR + "\\Driver\\geckodriver.exe")
            elif browser.lower() == "chrome":
                 driver = webdriver.Chrome(executable_path=ROOT_DIR +"\\Driver\\chromedriver.exe")
                #driver = webdriver.Firefox(
                #    executable_path="C:\\Users\\Dpkpc\\PycharmProjects\\OrangeHRMwithPytest\\Driver\\chromedriver.exe")
            else:
                raise Exception("Invalid Browser value provided")
            print(driver)
            return driver
        except:
            raise Exception(str(sys.exc_info()))
