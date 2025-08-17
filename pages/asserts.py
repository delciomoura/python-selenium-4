class ContactPageAsserts:

    def __init__(self, driver, page):
        self.driver = driver
        self.page = page

    def assert_login_page_title(self, expected_title):
        assert expected_title in self.driver.title, f"Esperado '{expected_title}' no título da página, mas foi '{self.driver.title}'"

    def assert_main_title(self, expected_text):
        main_title = self.page.get_main_title()
        assert expected_text in main_title, f"Esperado '{expected_text}' no título principal, mas foi '{main_title}'"

    def assert_contact_created(self, expected_name):
        contact_name = self.page.get_registered_contact_name()
        assert expected_name in contact_name, f"Esperado o nome '{expected_name}' no contato registrado, mas foi '{contact_name}'"

    def assert_text_validation(self, expect_notice_mame):
        contact_name_validation = self.page.get_element_text_validation_text()
        assert expect_notice_mame in contact_name_validation, f"Esperado o nome '{expect_notice_mame}' no contato registrado, mas foi '{contact_name_validation}'"
