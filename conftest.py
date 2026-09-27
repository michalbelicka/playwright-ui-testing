import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.cart_page import CartPage

@pytest.fixture
def home_page(page: Page):

    page.goto("https://www.automationexercise.com/")
    
    cookie_banner = page.get_by_role("button", name="Súhlas")

    if cookie_banner.is_visible():
        cookie_banner.click()

    return page

@pytest.fixture
def logged_in(home_page):

    signup_page = SignupPage(home_page)
    login_page = LoginPage(home_page)

    signup_page.click_signup_login()

    login_page.enter_login_details("tester2310@example.com", "password")
    
    login_page.click_login()

    return home_page

@pytest.fixture
def logged_in_and_empty_cart(logged_in):

    cart_page = CartPage(logged_in)

    cart_page.click_cart()

    cart_page.empty_cart()

    cart_page.close_ad()

    return logged_in
