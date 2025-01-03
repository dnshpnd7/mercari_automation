from pages.home_page import HomePage
from pages.category_page import CategoryPage


def wait_for_element(page, selector, timeout=5000):
    """
    Wait for an element to appear within a specified timeout.
    :param page: The Playwright page object
    :param selector: The CSS or XPath selector for the element
    :param timeout: The maximum time to wait for the element (default: 5000ms)
    """
    page.wait_for_selector(selector, timeout=timeout)


def test_mercari_search_conditions(page):
    # Instantiate Page Objects for HomePage and CategoryPage
    home_page = HomePage(page)
    category_page = CategoryPage(page)

    # Scenario 1: Select Categories and Validate Breadcrumbs
    # Navigate to the Mercari homepage
    page.goto("https://jp.mercari.com/")

    # Click on the search bar and open the category selection
    home_page.click_search_bar()
    home_page.click_select_by_category()

    # Select Tier 1, 2, and 3 categories
    category_page.select_tier1_category()
    category_page.select_tier2_category()
    category_page.select_tier3_category()

    # Retrieve and validate the breadcrumb text for selected categories
    breadcrumb_text = category_page.get_breadcrumb_text()
    print(f"Breadcrumb Text: {breadcrumb_text}")
    assert "本・雑誌・漫画" in breadcrumb_text, "Tier 1 category not set correctly"
    assert "本" in breadcrumb_text, "Tier 2 category not set correctly"
    assert "コンピュータ・IT" in breadcrumb_text, "Tier 3 category not set correctly"

    # Scenario 2: Validate Browsing History
    # Step 1: Return to the Mercari top page
    page.goto("https://jp.mercari.com/")

    # Step 2: Open the search bar
    home_page.click_search_bar()

    # Step 3: Check the browsing history count
    history_selector = "[data-testid='search-history']"
    wait_for_element(page, history_selector)
    history_entries = page.locator("div[data-testid='merListItem-container']")
    assert history_entries.count() == 2, "Expected 1 history entry"

    # Step 4: Verify and Click Latest Browsing History
    latest_history = history_entries.nth(0).inner_text()
    print(f"Latest History: {latest_history}")
    assert "コンピュータ・IT" in latest_history, "Latest history not showing correctly"

    # Click the saved browsing history entry
    saved_search = "//p[text()='コンピュータ・IT']"
    wait_for_element(page, saved_search)
    page.click(saved_search)

    # Step 5: Validate Breadcrumb After Clicking Browsing History
    updated_breadcrumb = category_page.get_breadcrumb_text()
    assert "本・雑誌・漫画" in updated_breadcrumb, "Tier 1 category not restored correctly"
    assert "本" in updated_breadcrumb, "Tier 2 category not restored correctly"
    assert "コンピュータ・IT" in updated_breadcrumb, "Tier 3 category not restored correctly"

    # Step 6: Perform a New Search with the term "javascript"
    search_input = "input[type='text']"
    page.fill(search_input, "javascript")
    page.keyboard.press("Enter")
    wait_for_element(page, "//h1[contains(text(),'javascript')]")

    # Step 7: Navigate back to the Mercari Top Page
    page.goto("https://jp.mercari.com/")

    # Step 8: Verify Browsing History Now Contains Three Entries
    home_page.click_search_bar()
    wait_for_element(page, history_selector)
    history_entries = page.locator("div[data-testid='merListItem-container']")
    assert history_entries.count() == 3, "Expected 3 history entries"

    # Step 9: Validate the Latest Browsing History Entry
    latest_history = history_entries.all_text_contents()
    print(f"All History Entries: {latest_history}")
    assert "javascript" in latest_history, "Latest history not showing 'javascript' correctly"
    assert "コンピュータ・IT" in latest_history, "Latest history category not showing correctly"

    # Final Confirmation
    print("All search conditions are set and validated successfully!")
