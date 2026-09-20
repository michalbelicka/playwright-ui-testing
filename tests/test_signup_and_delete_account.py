from pages.signup_page import SignupPage
import random
from playwright.sync_api import expect

def test_signup_and_delete_account(home_page, page):

    signup_page = SignupPage(page)
    
    signup_page.click_signup_login()

    assert signup_page.is_signup_section_visible()

    name = f"Tester{random.randint(1000, 9999)}"
    email = f"tester{random.randint(1000, 9999)}@example.com"
    password = "TestPassword123!"

    signup_page.enter_signup_details(name, email)

    signup_page.click_signup()

    expect(signup_page.account_information_heading()).to_be_visible()

    signup_page.select_title("Mr")

    expect(signup_page.select_radio("Mr")).to_be_checked()

    expect(signup_page.name_input()).to_have_value(name) == name

    expect(signup_page.email_input()).to_have_value(email) == email

    signup_page.password_input(password)

    signup_page.select_birt_day("5", "10", "1994")

    signup_page.newsletter_checkbox().check()

    expect(signup_page.newsletter_checkbox()).to_be_checked()

    signup_page.partner_offers_checkbox().check()

    expect(signup_page.partner_offers_checkbox()).to_be_checked()

    signup_page.fill_name("John", "Tester")
