from conftest import browser
from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.section.visible()
    accordion.section_Heading.click()
    time.sleep(2)
    assert not accordion.section.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.section_1.visible()
    assert not accordion.section_2.visible()
    assert not accordion.section_3.visible()

    
