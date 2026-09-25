from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_add_product_to_cart(logged_in):

    products_page = ProductsPage(logged_in)
    cart_page = CartPage(logged_in)

    cart_page.click_cart()

    cart_page.empty_cart()

    expect(cart_page.cart_is_empty_message()).to_be_visible()

    products_page.click_products()

    expect(products_page.all_products_heading()).to_be_visible()

    products_page.add_product_to_cart("Blue Top")