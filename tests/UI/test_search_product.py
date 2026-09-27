from pages.products_page import ProductsPage
from playwright.sync_api import expect

def test_search_product(home_page):

    products_page = ProductsPage(home_page)

    products_page.click_products()

    products_page.search_product("Winter Top")

    expect(products_page.searched_products_heading()).to_be_visible()

    expect(products_page.searched_product("Winter Top")).to_be_visible()