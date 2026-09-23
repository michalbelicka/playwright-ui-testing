from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login(home_page):

    signup_page = SignupPage(home_page)
    login_page = LoginPage(home_page)

    signup_page.click_signup_login()

    expect(login_page.login_section()).to_be_visible()

    login_page.enter_login_details("tester2310@example.com", "password")

    login_page.click_login()

    name = "Tester2310"
    expected_text = f"Logged in as {name}"

    expect(login_page.logged_in_as()).to_have_text(expected_text)



