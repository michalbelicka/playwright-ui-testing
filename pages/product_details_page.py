from playwright.sync_api import Page

class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page

    def product_name(self):
        return self.page.get_by_role("heading", name="Stylish")

    def product_price(self):
        return self.page.get_by_text("Rs. 1500")

    def availability(self):
        return self.page.get_by_text("Availability: In Stock")

    def condition(self):
        return self.page.get_by_text("Condition: New")

    def brand(self):
        return self.page.get_by_text("Brand: Madame")