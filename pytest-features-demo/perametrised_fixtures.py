import pytest

@pytest.fixture(params=["chrome", "firefox", "safari",'IE'])
def browser(request):
    return request.param

def test_launch_browser(browser):
    print(f'running the {browser} browser')
    assert browser in ['chrome', 'firefox', 'safari',"IE"]
