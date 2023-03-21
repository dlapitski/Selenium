import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)


try:
    # Find the input elements
    fname = browser.find_element(By.NAME, 'firstname')
    fname.send_keys('Michael')
    lname = browser.find_element(By.NAME, 'lastname')
    lname.send_keys('Smith')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('example@mail.com')

    # Get the path to the test file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'test_file.txt'
    file_path = os.path.join(current_dir, file_name)

    # Find the file element and send the test file
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    # Find submit button and click on it
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
