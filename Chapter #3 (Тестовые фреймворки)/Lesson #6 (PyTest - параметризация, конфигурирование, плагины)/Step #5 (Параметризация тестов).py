import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

link = 'https://stepik.org/lesson/236895/step/1'


@pytest.mark.parametrize('link_part', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_put_the_answer_into_the_field(browser, link_part):
    # Add implicit wait == 10 seconds
    browser.implicitly_wait(10)

    # Open a page
    browser.get(f'https://stepik.org/lesson/{link_part}/step/1')

    # Find a login button and click
    login_button = browser.find_element(By.CSS_SELECTOR, '#main-navbar #ember33')
    login_button.click()

    # Find email and password fields and fill them in with the values
    email = browser.find_element(By.CSS_SELECTOR, '#login_form [name="login"]')
    email.send_keys('...')  # here should be an email
    password = browser.find_element(By.CSS_SELECTOR, '#login_form [name="password"]')
    password.send_keys('...')  # here should be a password

    # Find login button and click
    login_button_in_form = browser.find_element(By.CSS_SELECTOR, 'button[class^="sign"]')
    login_button_in_form.click()

    # Check if there is one of the reset buttons and click it if found
    time.sleep(2)
    reset = browser.find_elements(By.XPATH, '//button[text()="Начать сначала (сброс)"]')
    solve_again = browser.find_elements(By.XPATH, '//button[text()="Решить снова"]')
    if reset:
        reset[0].click()
        ok = browser.find_element(By.XPATH, '//button[text()="OK"]')
        ok.click()
    elif solve_again:
        solve_again[0].click()

    # Find text area and fill it with the answer
    time.sleep(2)
    text_area = browser.find_element(By.CSS_SELECTOR, 'textarea[id^="ember"]')
    text_area.send_keys(str(math.log(int(time.time()))))

    # Find submit button, wait until it is enabled and click
    submit = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    WebDriverWait(browser, 2).until(
        expected_conditions.element_to_be_clickable(submit)
    )
    submit.click()

    # Find a clue on the page and make sure it's correct
    clue = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    if clue != 'Correct!':
        with open('result.txt', 'a') as file:
            file.write(clue)
    assert clue == 'Correct!', f'Clue part: {clue} |'
