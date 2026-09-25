from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_products(self):
        self.page.get_by_role("link", name="Products").click()

    def all_products_heading(self):
        return self.page.locator(".title.text-center", has_text="All Products")

    def add_product_to_cart(self, product_name):
        product = self.page.locator(".productinfo").filter(has_text=product_name)
        product.get_by_text("Add to cart").click()