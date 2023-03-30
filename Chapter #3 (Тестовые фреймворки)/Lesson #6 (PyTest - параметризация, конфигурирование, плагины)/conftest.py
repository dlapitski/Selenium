import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    firefox_options = FirefoxOptions()
    firefox_options.set_preference('intl.accept_languages', user_language)

    browser = None
    if browser_name == "chrome":
        print("\n...Start Chrome for test...")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\n...Start Firefox for test...")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n...Quit browser...")
    browser.quit()
