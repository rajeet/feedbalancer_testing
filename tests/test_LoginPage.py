

from Pages.LoginPage import LoginPage


def test_login_page_title(driver):
    login_page = LoginPage(driver)
    title = login_page.get_login_page_title("Feed Balancer")
    assert title == "Feed Balancer"


def test_login_using_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.do_login("admin@imali.media", "admin")
