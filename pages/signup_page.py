from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def click_signup_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()

    def is_signup_section_visible(self):
        return self.page.get_by_role("heading", name="New User Signup!").is_visible()

    def enter_signup_details(self, name, email):
        self.page.get_by_placeholder("name").fill(name)

        signup_form = self.page.locator(".signup-form")
        signup_form.get_by_placeholder("Email Address").fill(email)


        