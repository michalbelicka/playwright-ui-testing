from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def delivery_address_heading(self):
        return self.page.get_by_role("heading", name="Your delivery address")

    def billing_address_heading(self):
        return self.page.get_by_role("heading", name="Your billing address")

    def review_order_heading(self):
        return self.page.get_by_role("heading", name="Review Your Order")

    def product_name(self):
        return self.page.get_by_text("Blue Top")