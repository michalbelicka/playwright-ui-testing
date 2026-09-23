from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_logout(logged_in):

    login_page = LoginPage(logged_in)

    name = "Tester2310"
    expected_text = f"Logged in as {name}"

    expect(login_page.logged_in_as()).to_have_text(expected_text)

    login_page.click_logout()

    expect(login_page.login_section()).to_be_visible()