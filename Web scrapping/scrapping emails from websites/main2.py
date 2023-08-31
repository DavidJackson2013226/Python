from selenium import webdriver
import time
import re
PATH = 'C:\\Users\\1241891571583922\\Downloads\\chromedriver_win32\\chromedriver.exe'
l=list()
o={}
target_url = "https://www.randomlists.com/email-addresses"
driver=webdriver.Chrome()
driver.get(target_url)
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
html = driver.page_source
emails = re.findall(email_pattern, html)
time.sleep(5)
print(emails)
driver.close()