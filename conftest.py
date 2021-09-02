import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """Fixture for open browser driver and close
     him after every func."""
    browser = webdriver.Chrome()
    print(f'\nStart Chrome browser.')
    yield browser
    print("\nQuit browser.")
    browser.quit()
