import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # A wide desktop window, so Wikipedia shows the full search box in the header.
    return {**browser_context_args, "viewport": {"width": 1440, "height": 900}}
