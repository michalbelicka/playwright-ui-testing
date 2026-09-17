from pages.signup_page import SignupPage

def test_signup(home_page, page):

    signup_page = SignupPage(page)
    
    signup_page.click_signup_login()
    