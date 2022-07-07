import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get("https://www.google.com/gmail/about/")
element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,"//a[@data-action = 'sign in']")))
k = driver.find_element(By.XPATH,"//a[@data-action = 'sign in']")
if k:
    k.click()
else:
    print("Unable to click")
c = driver.find_element(By.XPATH,"//div[@class='VmOpGe']")
if c:
    print("Redirected to Login Page")
else:
    print("Unable to Access Login Page")
pdb.set_trace()
driver.close(30)
