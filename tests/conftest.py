import os

import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from python_skillbox.utils import attach
from dotenv import load_dotenv


DEFAULT_BROWSER = 'chrome'
DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        default=DEFAULT_BROWSER,
        help='web: browser (chrome | firefox)'
    )

    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
        help='web: browser version (if chrome: 100.0, 99.0; firefox: 98.0, 97.0)'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def get_option_browser_name(request):
    return request.config.getoption('--browser_name')


@pytest.fixture(scope='session')
def get_option_browser_version(request):
    return request.config.getoption('--browser_version')


@pytest.fixture(scope='function')
def setup_browser(get_option_browser_name, get_option_browser_version):
    browser.config.base_url = "https://skillbox.ru/"
    browser.config.window_width = 1440
    browser.config.window_height = 900
    browser.config.timeout = 15
    options = Options()

    browser_name = get_option_browser_name
    browser_name = browser_name if browser_name != '' else DEFAULT_BROWSER

    browser_version = get_option_browser_version
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
