from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def name_assert(self):

        try:
            self.find_element(locator='#user-name')#password
        except NoSuchElementException:
            return False
        return True

    def password_assert(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True
