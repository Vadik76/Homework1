"""Page Object for Wikipedia's search.

A "page object" keeps all the details about *how* to find things on the page
(selectors) in one place. Tests then read like plain steps:
    search_page.search_for("Software testing")
If Wikipedia changes its layout, only this file needs updating, not every test.
"""

from playwright.sync_api import Locator, Page

BASE_URL = "https://en.wikipedia.org"


class WikipediaSearchPage:
    def __init__(self, page: Page):
        self.page = page
        # The header search box. ":visible" skips hidden copies of the field.
        self.search_input: Locator = page.locator('input[name="search"]:visible').first
        # The suggestion list that drops down while typing.
        self.suggestions: Locator = page.get_by_role("option")
        # The big title at the top of any article or results page.
        self.heading: Locator = page.locator("#firstHeading")
        # Each item on the "Search results" page.
        self.results: Locator = page.locator(".mw-search-result")

    def open(self) -> None:
        self.page.goto(f"{BASE_URL}/wiki/Main_Page")

    def type_query(self, text: str) -> None:
        """Type letter by letter, like a real user (this triggers suggestions)."""
        self.search_input.click()
        self.search_input.press_sequentially(text, delay=50)

    def search_for(self, text: str) -> None:
        """Type the text and press Enter."""
        self.search_input.fill(text)
        self.search_input.press("Enter")
