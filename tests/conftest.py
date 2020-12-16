import pytest
import selenium as selenium
from selenium import webdriver


@pytest.fixture()
def driver():
    web_driver = selenium.webdriver.Chrome()
    # web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.get("http://staging-app.imali.media/")
    yield
    web_driver.quit()
