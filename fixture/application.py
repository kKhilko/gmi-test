from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import custom
from pages.accountPage import AccountPage
from pages.businessPage import BusinessPage
from pages.loginPage import LoginPage
from pages.session import SessionHelper


class Application:
    def __init__(self, browser):
        if browser == 'Chrome':
            self.wd = webdriver.Chrome(custom.chromedriver)
            self.wd.maximize_window()
        if browser == 'Firefox':
            self.wd = webdriver.Firefox(custom.geckodriver)

        # pages initializer in app
        self.session = SessionHelper(self)
        self.login_page = LoginPage(self)
        self.account_creation_page = AccountPage(self)
        self.business_creation_page = BusinessPage(self)
