from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_login_details(self, email, password):
        self.page.locator('[data-qa="login-email"]').fill(email)
        self.page.get_by_placeholder("Password").fill(password)

    def login_section(self):
        return self.page.get_by_role("heading", name="Login to your account")

    def click_login(self):
        self.page.get_by_role("button", name="Login").click()

    def logged_in_as(self):
        return self.page.locator("a", has_text="Logged in as")