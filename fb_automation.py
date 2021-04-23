# Facebook Login Using Selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
# open Google Chrome browser and download chrome driver based on version.
executable_path = 'C:\\Program Files (x86)\\chromedriver.exe'

driver = webdriver.Chrome(executable_path)
# maximize the window size
driver.maximize_window()
# delete the cookies
driver.delete_all_cookies()
# navigate to the url
driver.get("https://www.facebook.com")

# create a pass.txt file and add email and password
with open("pass.txt") as f:
    lines = f.readlines()
    user = driver.find_element_by_xpath('//*[@id="email"]').send_keys(lines[0].rstrip("\n"))
    time.sleep(1)
    password = driver.find_element_by_xpath('//*[@id="pass"]').send_keys(lines[1])
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').send_keys(Keys.ENTER)
    time.sleep(1)
# close the browser
driver.close()
print("facebook login has been successfully completed")
