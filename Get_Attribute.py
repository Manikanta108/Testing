from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators import Locators
import pdb

class Get:
    def __init__(self):
        #Initializing respective Webdriver
        self.driver = webdriver.Chrome()

    #Navigates to respective Webpage
    def launch(self):
        self.driver.implicitly_wait(0.5)
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")

    def input(self):
        #Find whether element is present or not using CSS SELECTOR
        #pdb.set_trace()
        element = self.driver.find_element(By.CSS_SELECTOR, Locators.ATTR)
        #If element is present display its value
        if element:
            print(element.get_attribute('name'))
        else:
            print("Unable to Get attribute")

        #Closes the webdriver
        self.driver.close()

# Create object to its respective class and call required functions
object = Get()
object.launch()
object.input()
