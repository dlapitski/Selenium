from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Math function
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    # Wait until the price is 100$
    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    # As soon as it is 100$, click the Book button
    button = browser.find_element(By.ID, 'book')
    button.click()

    # Find x value
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    # Fill the input field with a calculated value
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(calc(x))

    # Find and click a submit button
    submit = browser.find_element(By.CSS_SELECTOR, '.form-group .btn.btn-primary')
    submit.click()

    # Find an alert, get the correct value and print it here
    alert = browser.switch_to.alert
    value = alert.text.split()[-1]
    print(f'The answer is: {value}')

finally:
    browser.quit()
