from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https:/wikipedia.org")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//*[@id=\"search-form\"]/fieldset/button/i")

search_field.send_keys("Test Automation")
search_button.click()

assert "Test automation" in driver.title

driver.quit()
