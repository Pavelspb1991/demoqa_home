from conftest import browser
from selenium.webdriver.common.by import By


def test(browser):
    browser.get('https://www.saucedemo.com/')
    icon = browser.find_element(By.CSS_SELECTOR, "#icon")

    if icon is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")


def test_2(browser):
    browser.get('https://www.saucedemo.com/')
    login = browser.find_element(By.CSS_SELECTOR, "#user-name")

    if login is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")


def test_3(browser):
    browser.get('https://www.saucedemo.com/')
    password = browser.find_element(By.CSS_SELECTOR, "#password")

    if password is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")
