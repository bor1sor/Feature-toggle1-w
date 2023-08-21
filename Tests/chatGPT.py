from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open the web page
driver.get("https://www.example.com")

# Take a screenshot before refreshing the page
driver.save_screenshot("screenshot_before_refresh.png")

# Refresh the page
driver.refresh()

# Take a screenshot after refreshing the page
driver.save_screenshot("screenshot_after_refresh.png")

# Close the browser
driver.quit()
