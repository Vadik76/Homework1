Feature: Wikipedia search
  As a Wikipedia reader
  I want to search for articles
  So that I can quickly find the information I need

  Background:
    Given the Wikipedia main page is open

  # ---------------------------------------------------------------
  # POSITIVE: valid input, the feature does what it should
  # ---------------------------------------------------------------

  @positive
  Scenario Outline: Searching for an existing article opens it
    When I search for "<query>"
    Then the "<article>" article is shown

    Examples:
      | query                         | article                       |
      | Software testing              | Software testing              |
      | software testing              | Software testing              |
      | Python (programming language) | Python (programming language) |

  @positive
  Scenario: Suggestions appear while typing
    When I type "Software test" into the search field
    Then "Software testing" is shown in the suggestions

  @positive
  Scenario: A search with no exact match shows a list of results
    When I search for "automation testing tools"
    Then the search results page is shown
    And at least one result is listed

  # ---------------------------------------------------------------
  # NEGATIVE: invalid or unexpected input is handled safely
  # ---------------------------------------------------------------

  @negative
  Scenario: A nonsense search shows a "no results" message
    When I search for "qwxzvbnm plokijuh"
    Then the message "There were no results matching the query." is shown
    And no results are listed

  @negative
  Scenario Outline: Special characters and code do not break the search
    When I search for "<query>"
    Then the search results page is shown
    And no pop-up appears

    Examples:
      | query                         |
      | <script>alert('hi')</script>  |
      | ' OR 1=1 --                   |
      | %$#@!^&*                      |

  # ---------------------------------------------------------------
  # BOUNDARY: the edges of what the field accepts
  # (empty, shortest, longest allowed, one over the limit)
  # ---------------------------------------------------------------

  @boundary
  Scenario: An empty search does not open an article
    When I submit an empty search
    Then the search page is shown
    And no results are listed

  @boundary
  Scenario: A search of only spaces behaves like an empty search
    When I search for "   "
    Then the search page is shown
    And no results are listed

  @boundary
  Scenario: A one-character search works
    When I search for "A"
    Then the "A" article is shown

  @boundary
  Scenario: A search of exactly 300 characters (the maximum) is accepted
    When I search for a text that is 300 characters long
    Then the search results page is shown
    And the message "longer than the maximum allowed length" is not shown

  @boundary
  Scenario: A search of 301 characters (one over the maximum) is rejected
    When I search for a text that is 301 characters long
    Then the message "longer than the maximum allowed length" is shown
