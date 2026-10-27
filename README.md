# Wikipedia Search: UI Test Automation

A learning project: manual test cases for Wikipedia's search field, automated
with **Python + Playwright + pytest**, running on **GitHub Actions**.

## What's inside

| Path                          | What it is                                               |
|-------------------------------|----------------------------------------------------------|
| `docs/test_cases.md`          | Manual test cases (steps + expected results)             |
| `tests/test_search.py`        | The same test cases, automated                           |
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
pytest -v -k tc03            # run only one test case
```

If a test fails, look in the `test-results/` folder: there's a screenshot and a
trace. Open a trace with `playwright show-trace <path-to-trace.zip>` to replay
the test step by step.
