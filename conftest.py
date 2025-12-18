import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action='store',
        default="chrome",
        help="Browser to run tests : chrome/firefox/edge"
    )

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.demoblaze.com/')
    time.sleep(2)
    yield driver
    driver.close()
#############################################################################333

# @pytest.fixture(scope="class")
# def setup():
#     driver = webdriver.ChromeOptions()
#     driver.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(driver)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get("https://www.demoblaze.com/")
#     yield driver
#     driver.quit()