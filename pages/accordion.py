from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/accordian'
        self.section = WebElement(driver, "#section1Content > p ")
        self.section_Heading = WebElement(driver, "#section1Heading")
        self.section_1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.section_2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.section_3 = WebElement(driver, "#section3Content > p")
