import pytest
from selenium import webdriver
from pages.contact_save_page import ContactSavePage
from pages.asserts import ContactPageAsserts


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    contact_page = ContactSavePage(driver)
    asserts = ContactPageAsserts(driver, contact_page)
    yield driver, contact_page, asserts
    driver.quit()
