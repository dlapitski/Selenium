from math import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(log(abs(12*sin(int(x)))))


# Задание веб-драйвера и открытие браузера с сайтом
link = 'https://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

# Основной код авто-теста
try:
    # Находим элементы по селекторам
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    x = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute('valuex')
    answer_input.send_keys(calc(x))
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    # Находим кнопку Submit и отправляем данные формы на сервер
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

# Ожидание и закрытие браузерной сессии и теста
finally:
    time.sleep(10)
    browser.quit()