import time

from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, app):
        self.app = app

####################################################################################
#                                 Locators                                         #
####################################################################################
    button_link = '//a[@type="button"][text()="%s"]'
    footer_links = '//*[@class="links"]'

####################################################################################
#                                 Methods                                         #
####################################################################################

    def click_link_button(self, button_text):
        wd = self.app.wd
        self.app.session.close_modal_window('OK')
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(10)
        self.app.session.click_on_button(button_text)