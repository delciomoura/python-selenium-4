from fixtures.data_mass import data
import pytest


def test_save_contact(setup, create_user):
    driver, contact_page, asserts = setup
    user = create_user

    contact_page.visit_login_screen()
    asserts.assert_login_page_title(data["message"]["expectTitle"])
    contact_page.login(user["email"],
                       user["password"])

    asserts.assert_main_title(data["message"]["expectMessageAfterLogin"])
    contact_page.click_add_new_contact_button()
    contact_page.create_contact(
        data["contact"]["name"],
        data["contact"]["number"],
        data["contact"]["description"]
    )

    asserts.assert_contact_created(data["contact"]["name"])
    contact_page.click_remove_contact_button()


@pytest.mark.parametrize(
    "name, number, description, expected_message",
    [
        ("", data["contact"]["number"], data["contact"]
         ["description"], data["message"]["expectNoticeName"]),
        (data["contact"]["name"], "", data["contact"]
         ["description"], data["message"]["expectNoticePhone"]),
        (data["contact"]["name"], data["contact"]["number"],
         "", data["message"]["expectNoticeDescription"]),
    ]
)
def test_save_contact_with_invalid_fields(setup, name, number, description, expected_message, create_user):
    driver, contact_page, asserts = setup
    user = create_user

    contact_page.visit_login_screen()
    asserts.assert_login_page_title(data["message"]["expectTitle"])
    contact_page.login(user["email"],
                       user["password"])

    asserts.assert_main_title(data["message"]["expectMessageAfterLogin"])
    contact_page.click_add_new_contact_button()
    contact_page.create_contact(name, number, description)

    asserts.assert_text_validation(expected_message)
