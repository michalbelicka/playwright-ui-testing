import pytest
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page):

    page.goto("https://www.automationexercise.com/")
    
    cookie_banner = page.get_by_role("button", name="Súhlas")
    
    if cookie_banner.is_visible():
        cookie_banner.click()