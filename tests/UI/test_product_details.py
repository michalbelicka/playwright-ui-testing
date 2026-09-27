from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from playwright.sync_api import expect

def test_product_details(home_page):

    products_page = ProductsPage(home_page)
    product_details_page = ProductDetailsPage(home_page)

    products_page.view_product("Stylish Dress")

    expect(product_details_page.product_name()).to_have_text("Stylish Dress")

    expect(product_details_page.product_price()).to_have_text("Rs. 1500")

    expect(product_details_page.availability()).to_have_text("Availability: In Stock")

    expect(product_details_page.condition()).to_have_text("Condition: New")

    expect(product_details_page.brand()).to_have_text("Brand: Madame")