from selenium.webdriver.common.by import By
from pages.elements_page import ElementsPage


class ContactSavePage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = ElementsPage(driver)

    def visit_login_screen(self):
        self.driver.get("http://localhost:8080/")

    def login(self, username, password):
        self.elements.get_name_field().send_keys(username)
        self.elements.get_password_field().send_keys(password)
        self.elements.get_sigIn_button().click()

    def search(self, text):
        self.driver.find_element(*self.search_box).send_keys(text + "\n")

    def create_contact(self, name, number, description):
        self.elements.get_contact_name().send_keys(name)
        self.elements.get_contact_number().send_keys(number)
        self.elements.get_contact_description().send_keys(description)
        self.elements.get_save_button().click()

    def get_main_title(self):
        return self.elements.h4_element().text

    def click_add_new_contact_button(self):
        self.elements.add_new_contact_button().click()

    def get_registered_contact_name(self):
        return self.elements.get_contact_name_registred().text
    
    def click_remove_contact_button(self):
        self.elements.get_remove_button().click()
    
    def get_element_text_validation_text(self):
        return self.elements.get_element_text_validation().text
