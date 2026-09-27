from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_invalid_login(home_page):

    signup_page = SignupPage(home_page)
    login_page = LoginPage(home_page)

    signup_page.click_signup_login()

    login_page.enter_login_details("wrongmail@example.com", "wrong_password")

    login_page.click_login()

    expect(login_page.login_error()).to_be_visible()