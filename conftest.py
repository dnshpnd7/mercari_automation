import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    """Create a Playwright instance for the session."""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch the browser for the session."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Create a new browser context and page for each test function."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")  # Access the page fixture
        if page:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            pytest_html = getattr(item.config, "_html", None)
            if pytest_html:
                extra = getattr(pytest_html, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
