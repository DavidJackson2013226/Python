from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.
driver = webdriver.Chrome()
  
# get https://www.geeksforgeeks.org/
driver.get("https://fireant.vn/charts")
print(driver.text)
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(60)

# Obtain button by link text and click.
button = driver.find_element(By.LINK_TEXT, 'Thêm mã CK')
button.click()