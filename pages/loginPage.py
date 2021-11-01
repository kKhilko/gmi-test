from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, app):
        self.app = app

####################################################################################
#                                 Locators                                         #
####################################################################################
    button_link = '//a[@type="button"][text()="%s"]'

    def click_link_button(self, button_text):
        wd = self.app.wd
        wd.find_element(By.XPATH, self.button_link % button_text).click()