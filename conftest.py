import pytest
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page):

    page.goto("https://www.automationexercise.com/")
    
