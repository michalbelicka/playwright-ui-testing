from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def click_signup_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()
    