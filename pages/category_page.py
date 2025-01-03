import time

from pages.base_page import BasePage

class CategoryPage(BasePage):
    TIER1_CATEGORY_SELECTOR = "//a[text()='本・雑誌・漫画']"
    TIER2_CATEGORY_SELECTOR = "//a[text()='本']"
    TIER3_CATEGORY_SELECTOR = "//a[text()='コンピュータ・IT']"
    BREADCRUMB_SELECTOR = "//div[@id='search-filter']//child::li"

    def select_tier1_category(self):
        self.wait_and_click(self.TIER1_CATEGORY_SELECTOR)

    def select_tier2_category(self):
        self.wait_and_click(self.TIER2_CATEGORY_SELECTOR)

    def select_tier3_category(self):
        self.wait_and_click(self.TIER3_CATEGORY_SELECTOR)

    def get_breadcrumb_text(self):
        return self.get_text(self.BREADCRUMB_SELECTOR)
