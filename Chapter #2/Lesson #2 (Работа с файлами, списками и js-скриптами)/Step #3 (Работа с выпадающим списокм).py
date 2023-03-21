import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Find num1 & num2 values
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text

    # Find total of the values
    total = [int(num1) + int(num2)]

    # Find select element and select a correct option (total)
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(list(map(lambda x: str(x), total))[0])

    # Find and click the Submit button
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
