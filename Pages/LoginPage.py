from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME_ELEMENT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_ELEMENT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'btn px-4')]")


    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_ELEMENT, username)
        self.do_send_keys(self.PASSWORD_ELEMENT, password)
        self.do_click(self.LOGIN_BUTTON)






