from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_product_total_price_based_on_quantity(empty_cart):

    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    
    products_page.click_products()
    
    products_page.add_product_to_cart("Blue Top")
    
    products_page.click_view_cart()

    price_text = cart_page.product_total_price("Blue Top").inner_text()

    unit_price = int(price_text.replace("Rs. ", ""))

    assert unit_price == 500

    expected_total = unit_price * 2

    products_page.click_products()
        
    products_page.add_product_to_cart("Blue Top")
        
    products_page.click_view_cart()

    expect(cart_page.product_total_price("Blue Top")).to_have_text(f"Rs. {expected_total}")



