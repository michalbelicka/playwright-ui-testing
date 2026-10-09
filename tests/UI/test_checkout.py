from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_checkout(logged_in_with_product):

    cart_page = CartPage(logged_in_with_product)
    checkout_page = CheckoutPage(logged_in_with_product)

    expect(cart_page.product_in_cart("Blue Top")).to_be_visible()

    cart_page.click_proceed_to_checkout()

    expect(checkout_page.delivery_address_heading()).to_be_visible()

    expect(checkout_page.billing_address_heading()).to_be_visible()

    expect(checkout_page.review_order_heading()).to_be_visible()

    expect(checkout_page.product_name()).to_be_visible()