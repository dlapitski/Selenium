import time
from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# Math function
def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

# Main section
try:
    # Find and click a button
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()

    # Find and accept an alert
    alert = browser.switch_to.alert
    alert.accept()

    # Find x value
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    # Fill the input field with a calculated value
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(calc(x))

    # Find and click a submit button
    submit = browser.find_element(By.CSS_SELECTOR, '.form-group .btn.btn-primary')
    submit.click()

    # Little break before an alert appears
    time.sleep(5)

    # Find an alert, get the correct value and print it here
    alert = browser.switch_to.alert
    value = alert.text.split()[-1]
    print(value)

finally:
    browser.quit()