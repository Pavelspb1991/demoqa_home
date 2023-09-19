from pages.base_page import BasePage
from components.components import WebElement


class Modal_dialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/modal-dialogs'
        self.modal = WebElement(driver, "#item-")
