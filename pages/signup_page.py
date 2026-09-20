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

    def click_signup(self):
        self.page.get_by_role("button", name="Signup").click()

    def account_information_heading(self):
        return self.page.locator(".title.text-center", has_text="Enter Account Information")

    def select_title(self, title):
        self.page.locator(f'input[type="radio"][value={title}]').check()

    def select_radio(self, title):
        return self.page.locator(f'input[type="radio"][value={title}]')

    def name_input(self):
        return self.page.locator('[data-qa="name"]')

    def email_input(self):
        return self.page.locator('[data-qa="email"]')

    def password_input(self, password):
        self.page.locator('[data-qa="password"]').fill(password)

    def select_birt_day(self, day, month, year):
        self.page.locator("#days").select_option(day)
        self.page.locator("#months").select_option(month)
        self.page.locator("#years").select_option(year)

    def newsletter_checkbox(self):
        return self.page.locator("#newsletter")

    def partner_offers_checkbox(self):
        return self.page.locator("#optin")

    def fill_name(self, first_name, last_name):
        self.page.locator("#first_name").fill(first_name)
        self.page.locator("#last_name").fill(last_name)