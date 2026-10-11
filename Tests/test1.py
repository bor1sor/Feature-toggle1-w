from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup webdriver
driver = webdriver.Chrome()

# navigate to apple.com and wait for page to load
driver.get("https://www.apple.com/")
time.sleep(2)

# refresh page
driver.refresh()
time.sleep(2)

# navigate to walmart.com and wait for page to load
driver.get("https://www.walmart.com/")
time.sleep(2)

# take screenshot
driver.save_screenshot("walmart_screenshot.png")

# close browser window
driver.quit()
