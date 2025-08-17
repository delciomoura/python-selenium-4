from selenium import webdriver
from pages.contact_save_page import ContactSavePage
from pages.asserts import ContactPageAsserts
from fixtures.data_mass import data


def test_contact_save():
    driver = webdriver.Chrome()
    contact_page = ContactSavePage(driver)
    asserts = ContactPageAsserts(driver, contact_page)

    contact_page.visit_login_screen()

    asserts.assert_login_page_title(data["message"]["expectTitle"])
    contact_page.login(data["parameters"]["validUser"],
                       data["parameters"]["validPassword"])

    asserts.assert_main_title(data["message"]["expectMessageAfterLogin"])
    contact_page.click_add_new_contact_button()
    contact_page.create_contact(
        data["contact"]["name"],
        data["contact"]["number"],
        data["contact"]["description"]
    )

    asserts.assert_contact_created(data["contact"]["name"])
    contact_page.click_remove_contact_button()

    driver.quit()
