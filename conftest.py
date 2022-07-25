import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", help="Choose browser")
    parser.addoption("--base_url")
    parser.addoption("--executor")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--bv")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise pytest.UsageError("--browser_name должен быть chrome, firefox или opera")

    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                               options=options,
                               desired_capabilities={
                                   "BrowserName": browser_name,
                                   "browserVersion": version,
                                   "selenoid:options": {
                                       "enableVNC": vnc
                                   }
                               }
                               )

    yield browser
    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
