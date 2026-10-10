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

    def product_name(self, product_name):
        return self.page.get_by_text(product_name)

    def enter_order_comment(self, order_comment):
        self.page.locator('textarea[name="message"]').fill(order_comment)

    def click_place_order(self):
        self.page.get_by_role("link", name="Place Order").click()
