from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def h4_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h4"))
        )

    def add_new_contact_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="addNewContact"]'))
        )

    def get_contact_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="name"]'))
        )

    def get_contact_number(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="number"]'))
        )

    def get_contact_description(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="description"]'))
        )

    def get_save_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="saveButton"]'))
        )

    def get_contact_name_registred(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[class="media-content"] [class="title is-4"]'))
        )

    def get_remove_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-cy="btn-remove"]'))
        )
    
    def get_name_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.NAME, "email"))
        )
    
    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.NAME, "password"))
        )
    
    def get_sigIn_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "sigIn"))
        )
    
    def get_element_text_validation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[class="has-text-danger"]'))
        )
