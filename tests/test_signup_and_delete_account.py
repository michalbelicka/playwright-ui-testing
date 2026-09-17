from pages.signup_page import SignupPage

def test_signup_and_delete_account(home_page, page):

    signup_page = SignupPage(page)
    
    signup_page.click_signup_login()

    assert signup_page.is_signup_section_visible()

    signup_page.enter_signup_details("Tester", "tester@email.com")