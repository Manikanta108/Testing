from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators import Locators
#import time


class Input:
    #Initializing the respective web browser
    def __init__(self):
        self.driver = webdriver.Chrome()
    #Navigate to webpage
    def launch(self):
        self.driver.implicitly_wait(0.5)
        self.driver.maximize_window()
        self.driver.get('https://www.facebook.com/')
    #Function to enter input to the textbox
    def input(self):
        #Validate Email textbox is visible or not
        email = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locators.EMAIL)))
        email = self.driver.find_element(By.XPATH, Locators.EMAIL)
        #Enter input text to Email textbox
        if email:
            email.send_keys('jwalaunique563@gmail.com')
        else:
            print('Unable to take Email')
        # Validate password textbox is visible or not
        password = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locators.PASSWORD)))
        password = self.driver.find_element(By.XPATH, Locators.PASSWORD)
        # Enter input text to password textbox
        if password:
            password.send_keys('12345678')
        else:
            print('Unable to take Password')

# Create object to its respective class and call required functions
inp = Input()
inp.launch()
inp.input()
