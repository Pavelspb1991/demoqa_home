from conftest import browser
from pages.swag_labs import SwagLabs
from pages.base_page import BasePage


def test(browser):
    icon = BasePage(browser)
    icon_2 = SwagLabs(browser)
    icon.visit()
    assert icon_2.exist_icon()



def test_2(browser):
    icon = BasePage(browser)
    icon_2 = SwagLabs(browser)
    icon.visit()
    assert icon_2.name_assert()


def test_3(browser):
   icon = BasePage(browser)
   icon_2 = SwagLabs(browser)
   icon.visit()
   assert icon_2.password_assert()