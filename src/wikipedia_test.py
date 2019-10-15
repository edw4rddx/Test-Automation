from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https:/wikipedia.org")

    search_field = driver.find_element_by_id("searchInput")
    search_button = driver.find_element_by_xpath("//*[@id=\"search-form\"]/fieldset/button/i")

    search_text = "Test automation"
    search_field.send_keys(search_text)
    search_button.click()

    # Positive test cases
    # Test browser caption
    assert search_text in driver.title

    # Test article header
    article_header = driver.find_element_by_xpath("//*[@id=\"firstHeading\"]")
    assert search_text in article_header.text

    # Negative test case
    # Test article contents
    article_contents = driver.find_element_by_class_name("toc")
    assert "Manual testing" in article_contents.text
    
finally:
    driver.quit()
