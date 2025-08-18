import pytest
import requests
from selenium import webdriver
from pages.contact_save_page import ContactSavePage
from pages.asserts import ContactPageAsserts
import faker

faker = faker.Faker("pt_BR")


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    contact_page = ContactSavePage(driver)
    asserts = ContactPageAsserts(driver, contact_page)
    yield driver, contact_page, asserts
    driver.quit()

BASE_URL = "http://localhost:3000"

@pytest.fixture
def create_user():
    """Cria um usuário na API antes do teste"""
    user = {
        "email": faker.email(),
        "password": "delcio123"
    }

    response = requests.post(
        f"{BASE_URL}/user",
        json=user,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code in [200, 201], f"Erro ao criar usuário: {response.text}"
    return user