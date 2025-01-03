from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR_SELECTOR = "//input[@placeholder='なにをお探しですか？']"
    CATEGORY_BUTTON_SELECTOR = "a[href='/categories'] p"

    def click_search_bar(self):
        self.wait_and_click(self.SEARCH_BAR_SELECTOR)

    def click_select_by_category(self):
        self.wait_and_click(self.CATEGORY_BUTTON_SELECTOR)
