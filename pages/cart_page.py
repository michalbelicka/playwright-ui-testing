from playwright.sync_api import Page

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

            delete_buttons.first.click()

            