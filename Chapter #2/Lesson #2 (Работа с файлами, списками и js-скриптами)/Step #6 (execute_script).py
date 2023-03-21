import time
from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# Calculate the x value and return it as a string
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Find x value
    x = browser.find_element(By.ID, 'input_value').text

    # Find an input field and fill it with the x value
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(calc(x))

    # Find checkbox and select the correct options
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][id="robotCheckbox"]')
    checkbox.click()

    # Find radio and scroll the page to get to the overlapped radio
    radio = browser.find_element(By.CSS_SELECTOR, 'input[type="radio"][id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Scroll the page to get to the overlapped Submit button
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    # Click the Submit button
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
