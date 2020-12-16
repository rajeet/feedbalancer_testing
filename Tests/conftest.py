import pytest
from selenium import webdriver



@pytest.fixture(scope='class')
def init_driver():
    web_driver = webdriver.Chrome(executable_path="/home/rajeet/chromedriver")
    # web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.get("http://staging-app.imali.media/")
    yield
    web_driver.quit()
