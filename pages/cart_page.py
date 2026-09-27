from playwright.sync_api import Page
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def click_cart(self):
        self.page.get_by_role("link", name="Cart").click()

    def cart_is_empty_message(self):
        return self.page.locator(".text-center", has_text="Cart is empty!")

    def empty_cart(self):
        delete_buttons = self.page.locator(".cart_quantity_delete")

        while delete_buttons.count() > 0:
            current_count = delete_buttons.count()

            delete_buttons.first.click(force=True)

            expect(delete_buttons).to_have_count(current_count - 1)


    def product_in_cart(self, product_name):
        return self.page.locator(".cart_description", has_text=product_name)

    def close_ad(self):
        close_button = self.page.locator("#dismiss-button")

        if close_button.is_visible():
            close_button.click()

    def remove_product(self, product_name):
        product = self.page.locator("#cart_info", has_text=product_name)

        product.locator(".cart_quantity_delete").click()

            