# Wikipedia Search: UI Test Automation

A learning project: BDD test scenarios for Wikipedia's search field, written in
**Gherkin** (Given / When / Then) and automated with **Python + Playwright +
pytest-bdd**, running on **GitHub Actions**.

pytest-bdd is the Python equivalent of Cucumber: same `.feature` files, same
Gherkin syntax.

## What's inside

| Path                          | What it is                                               |
|-------------------------------|----------------------------------------------------------|
| `features/search.feature`    | The test scenarios in Gherkin (positive / negative / boundary) |
| `tests/test_search_steps.py`  | Step definitions: the code behind each Given/When/Then line |
| `pages/search_page.py`        | Page Object: where the search box, results etc. are found |
| `conftest.py`, `pytest.ini`   | Test settings (window size, screenshots on failure)      |
| `.github/workflows/tests.yml` | Runs all tests on GitHub on every push                   |

## Run it on your computer

You need Python 3.10 or newer (https://www.python.org/downloads/).

```bash
# 1. Create an isolated Python environment (one time)
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Mac / Linux:  source .venv/bin/activate

# 2. Install the tools and a browser (one time)
pip install -r requirements.txt
playwright install chromium

# 3. Run the tests
pytest -v                    # all tests, browser hidden
pytest -v --headed           # watch the browser do it
pytest -v --headed --slowmo 500   # watch it, slowed down
pytest -v -m positive        # only scenarios tagged @positive
pytest -v -m "negative or boundary"
pytest -v -k suggestions     # only scenarios with "suggestions" in the name
```

If a test fails, look in the `test-results/` folder: there's a screenshot and a
trace. Open a trace with `playwright show-trace <path-to-trace.zip>` to replay
the test step by step.
