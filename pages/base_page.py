from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_and_click(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def get_text(self, selector: str):
        self.page.wait_for_selector(selector)
        return self.page.text_content(selector)
