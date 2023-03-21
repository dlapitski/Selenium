from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Используй http://suninjuly.github.io/registration1.html для теста №1
    # и http://suninjuly.github.io/registration2.html для теста №2
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, 'input[class="form-control first"][required]')
    first_name.send_keys('Mike')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[class="form-control second"][required]')
    last_name.send_keys('Smith')
    email = browser.find_element(By.CSS_SELECTOR, 'input[class="form-control third"][required]')
    email.send_keys('example@mail.com')
    phone = browser.find_element(By.CSS_SELECTOR, 'input:not(input[required])[class="form-control first"]')
    phone.send_keys('8 800 555 35 35')
    address = browser.find_element(By.CSS_SELECTOR, 'input:not(input[required])[class="form-control second"]')
    address.send_keys('NY Main Street 255/55, 243')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()