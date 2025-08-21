import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium", help="browser selection: chrome or firefox")

@pytest.fixture(scope="module")
def page(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch()
    elif browser_name == "firefox":
        browser = playwright.firefox.launch()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    page.close()


