from pages.modal_dialogs import Modal_dialogs
from conftest import browser
def test_modal_elements(browser):
    modal = Modal_dialogs(browser)
    modal.visit()
    assert modal.modal.check_count_elements(5)
