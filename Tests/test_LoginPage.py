import pytest

from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_Login(BaseTest):
    def __init__(self):
        pass
        
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title("Feed Balancer")
        assert title == "Feed Balancer"

    def test_login_using_valid_credentials(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("admin@imali.media", "admin")
