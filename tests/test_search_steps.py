"""Step definitions: the Python code behind each Given / When / Then line
in features/search.feature.

How it works:
  - Each @given / @when / @then below matches one line of the feature file.
  - Text in {curly braces} is captured from the line and passed in,
    e.g. 'I search for "Software testing"' gives query="Software testing".
  - `expect(...)` is a check. If it's not true within a few seconds, the step fails.
"""

import re

from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.search_page import WikipediaSearchPage

# Turn every scenario in the feature file into a pytest test.
scenarios("../features/search.feature")


# ----------------------------- Given -----------------------------

@given("the Wikipedia main page is open", target_fixture="search_page")
def open_main_page(page: Page) -> WikipediaSearchPage:
    search_page = WikipediaSearchPage(page)
    search_page.open()
    return search_page


# ----------------------------- When ------------------------------

@when(parsers.parse('I search for "{query}"'))
def search_for(search_page: WikipediaSearchPage, query: str):
    search_page.search_for(query)


@when("I submit an empty search")
def submit_empty_search(search_page: WikipediaSearchPage):
    search_page.search_for("")


@when(parsers.parse("I search for a text that is {length:d} characters long"))
def search_for_text_of_length(search_page: WikipediaSearchPage, length: int):
    search_page.search_for("a" * length)


@when(parsers.parse('I type "{text}" into the search field'))
def type_into_search(search_page: WikipediaSearchPage, text: str):
    search_page.type_query(text)


# ----------------------------- Then ------------------------------

@then(parsers.parse('the "{title}" article is shown'))
def article_is_shown(search_page: WikipediaSearchPage, title: str):
    expect(search_page.heading).to_have_text(title)
    expect(search_page.page).not_to_have_url(re.compile("Special:Search"))


@then(parsers.parse('"{title}" is shown in the suggestions'))
def suggestion_is_shown(search_page: WikipediaSearchPage, title: str):
    expect(search_page.suggestions.filter(has_text=title).first).to_be_visible()


@then("the search results page is shown")
def results_page_is_shown(search_page: WikipediaSearchPage):
    expect(search_page.heading).to_have_text("Search results")


@then("the search page is shown")
def search_page_is_shown(search_page: WikipediaSearchPage):
    expect(search_page.page).to_have_url(re.compile("Special(:|%3A)Search"))


@then("at least one result is listed")
def at_least_one_result(search_page: WikipediaSearchPage):
    expect(search_page.results.first).to_be_visible()


@then("no results are listed")
def no_results(search_page: WikipediaSearchPage):
    expect(search_page.results).to_have_count(0)


@then(parsers.parse('the message "{text}" is shown'))
def message_is_shown(search_page: WikipediaSearchPage, text: str):
    expect(search_page.page.get_by_text(text)).to_be_visible()


@then(parsers.parse('the message "{text}" is not shown'))
def message_is_not_shown(search_page: WikipediaSearchPage, text: str):
    expect(search_page.page.get_by_text(text)).to_have_count(0)


@then("no pop-up appears")
def no_popup(search_page: WikipediaSearchPage):
    assert search_page.popups == [], f"A pop-up appeared, so the script ran: {search_page.popups}"
