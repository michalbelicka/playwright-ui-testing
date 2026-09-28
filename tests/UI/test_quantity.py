from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_product_quantity(empty_cart):

    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)

    products_page.click_products()

    products_page.add_product_to_cart("Blue Top")

    products_page.click_view_cart()

    expect(cart_page.product_quantity("Blue Top")).to_have_text("1")

    products_page.click_products()
    
    products_page.add_product_to_cart("Blue Top")
    
    products_page.click_view_cart()

    expect(cart_page.product_quantity("Blue Top")).to_have_text("2")



