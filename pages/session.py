from selenium.webdriver.common.by import By


class SessionHelper:
    '''
    Session class initialize:
    open landing page,
    validate session,
    session quit
    '''

    def __init__(self, app):
        self.app = app

    modal = 'cookiePolicyAgreement'
    button_link = '//a[@type="button"][text()="%s"]'

    def open_landing_page(self, url):
        wd = self.app.wd
        wd.get(url)

    def is_valid(self):
        try:
            self.get_url()
            return True
        except:
            return False

    def session_destroy(self):
        self.app.wd.quit()

    def click_on_button(self, btn_text):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, self.button_link % btn_text)
        wd.execute_script("arguments[0].click();", element)

    def close_modal_window(self, btn_text):
        wd = self.app.wd
        modals = wd.find_elements(By.ID, self.modal)
        if len(modals)>0:
            self.click_on_button(btn_text)

    def get_url(self):
        return self.app.wd.current_url

    def reload_a_page(self):
        self.app.wd.refresh()

