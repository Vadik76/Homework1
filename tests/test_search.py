"""Automated versions of the test cases in docs/test_cases.md.

How to read a test:
  - `page` is a browser tab that pytest-playwright opens for us.
  - `expect(...)` is a check. If it's not true within a few seconds, the test fails.
"""

import re

import pytest
from playwright.sync_api import Page, expect

from pages.search_page import WikipediaSearchPage


@pytest.fixture
def search_page(page: Page) -> WikipediaSearchPage:
    """Precondition shared by every test: Wikipedia main page is open."""
    search_page = WikipediaSearchPage(page)
    search_page.open()
    return search_page


def test_tc01_existing_article_opens(search_page: WikipediaSearchPage):
    search_page.search_for("Software testing")

    expect(search_page.heading).to_have_text("Software testing")
    expect(search_page.page).to_have_url(re.compile(r"/wiki/Software_testing$"))


# "parametrize" runs the same test once per value: one test, many inputs.
@pytest.mark.parametrize("query", ["Software testing", "software testing"])
def test_tc02_lowercase_first_letter_finds_same_article(
    search_page: WikipediaSearchPage, query: str
):
    search_page.search_for(query)

    expect(search_page.heading).to_have_text("Software testing")


def test_tc03_suggestions_appear_while_typing(search_page: WikipediaSearchPage):
    search_page.type_query("Software test")

    expect(search_page.suggestions.filter(has_text="Software testing").first).to_be_visible()


def test_tc04_no_exact_match_shows_result_list(search_page: WikipediaSearchPage):
    search_page.search_for("automation testing tools")

    expect(search_page.heading).to_have_text("Search results")
    expect(search_page.results.first).to_be_visible()


def test_tc05_nonsense_query_shows_no_results_message(search_page: WikipediaSearchPage):
    search_page.search_for("qwxzvbnm plokijuh")

    expect(search_page.page.get_by_text("There were no results matching the query.")).to_be_visible()
    expect(search_page.results).to_have_count(0)


def test_tc06_script_in_query_is_not_executed(search_page: WikipediaSearchPage):
    popups = []
    # If any alert/confirm pop-up shows up, remember it and close it.
    search_page.page.on("dialog", lambda dialog: (popups.append(dialog.message), dialog.dismiss()))

    search_page.search_for("<script>alert('hi')</script>")

    expect(search_page.heading).to_have_text("Search results")
    assert popups == [], f"A pop-up appeared, so the script ran: {popups}"
