from pages.signup_page import SignupPage
from pages.login_page import LoginPage
import random
from playwright.sync_api import expect

def test_signup_and_delete_account(home_page):

    expect(home_page).to_have_url("https://www.automationexercise.com/")
    
    signup_page = SignupPage(home_page)
    login_page = LoginPage(home_page)
    
    signup_page.click_signup_login()

    expect(signup_page.signup_section()).to_be_visible()

    name = f"Tester{random.randint(1000, 9999)}"
    email = f"tester{random.randint(1000, 9999)}@example.com"
    password = "TestPassword123!"

    signup_page.enter_signup_details(name, email)

    signup_page.click_signup()

    expect(signup_page.account_information_heading()).to_be_visible()

    signup_page.select_title("Mr")

    expect(signup_page.select_radio("Mr")).to_be_checked()

    expect(signup_page.name_input()).to_have_value(name)

    expect(signup_page.email_input()).to_have_value(email)

    signup_page.password_input(password)

    signup_page.select_birth_date("5", "10", "1994")

    signup_page.newsletter_checkbox().check()

    expect(signup_page.newsletter_checkbox()).to_be_checked()

    signup_page.partner_offers_checkbox().check()

    expect(signup_page.partner_offers_checkbox()).to_be_checked()

    signup_page.fill_name("John", "Tester")

    signup_page.fill_company("Test company")

    signup_page.fill_address("123 Test Street", "Apartment 4B")

    signup_page.select_country("United States")

    signup_page.fill_state_and_city("California", "Los Angeles")

    signup_page.fill_zipcode("90001")

    signup_page.fill_mobile_number("2135550147")

    signup_page.click_create_account()

    expect(signup_page.account_created_message()).to_have_text("Account Created!")

    signup_page.click_continue()

    expected_text = f"Logged in as {name}"

    expect(login_page.logged_in_as()).to_have_text(expected_text)

    signup_page.click_delete_account()

    expect(signup_page.account_deleted_message()).to_have_text("Account Deleted!")