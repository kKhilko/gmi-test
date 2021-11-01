import random
import time

from selenium.webdriver.common.by import By


class BusinessPage:
    def __init__(self, app):
        self.app = app

####################################################################################
#                                 Locators                                         #
####################################################################################
    page_logo = '//img[@alt="Gemini"]'
    form_title = '//div[@class="FormHeader"]/h3'
    form_body = '//form'
    form_fieldsets = '//fieldset'
    page_footer = 'GeminiSimpleFooter'

    all_inputs = '//label[@data-testid="undefined-label"]//input'
    input_field_by_name = '//input[@name="%s"]'
    all_input_highlighted_labels = '//label[@data-testid="undefined-label"]/div[@color]'
    input_field_label_by_name = '//label/div[//input[@name="%s"]]'

    dropdown_arrow_by_field_name = '//label[./div[text()="%s"]]//div[contains(@class,"Dropdown__indicators")]'
    dropdown_all_options = '//div[contains(@class,"Dropdown__option")]/div'
    dropdown_option = '//div[contains(@class,"Dropdown__option")]/div[text()="%s"]'
    dropdown_value_container_by_field_name = '//label[./div[text()="%s"]]//div[contains(@class,"Dropdown__value-container")]'

    alert_body_components = '//div[@class="AlertBody"]//li'

    continue_btn = '//button[@type="submit"]'

####################################################################################
#                                 Methods                                         #
####################################################################################
    def open_business_registration_form(self):
        self.app.session.open_landing_page(url='https://exchange.sandbox.gemini.com/')
        self.app.login_page.click_link_button('Create new account')
        self.app.account_creation_page.click_link_button('Create a business account')

    def is_logo_present(self):
        wd = self.app.wd
        return True if len(wd.find_elements(By.XPATH, self.page_logo)) == 1 else False

    def get_form_fieldsets(self):
        wd = self.app.wd
        fieldsets = wd.find_elements(By.XPATH, self.form_fieldsets)
        return [i.get_attribute('name') for i in fieldsets]

    def get_form_title(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, self.form_title).text

    def is_form_present(self):
        wd = self.app.wd
        return True if len(wd.find_elements(By.XPATH, self.form_body)) == 1 else False

    def is_page_footer_present(self):
        wd = self.app.wd
        return True if len(wd.find_elements(By.ID, self.page_footer)) == 1 else False

    def is_business_register_page_open(self):
        return True if '/register/institution' in self.app.session.get_url() else False

    def click_continue(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.find_element(By.XPATH, self.continue_btn).click()

#####################  Input field ##########################
    # implement input complete for specific field
    def complete_business_name_input_field(self, value):
        wd = self.app.wd
        wd.find_element(By.XPATH, self.input_field_by_name % 'company.legalName').send_keys(value)

    # implement input complete for any field by name
    def complete_input_field(self, field_name, value):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.find_element(By.XPATH, self.input_field_by_name % field_name).send_keys(value)

    def get_field_value(self, input_field):
        wd = self.app.wd
        return wd.find_element(By.XPATH, self.input_field_by_name % input_field).get_attribute('value')

    def get_input_field_label(self, input_field):
        wd = self.app.wd
        return wd.find_element(By.XPATH, self.input_field_label_by_name % input_field)

    def get_all_error_input_labels(self) -> list:
        wd = self.app.wd
        alert = wd.find_elements(By.XPATH, self.all_input_highlighted_labels)
        return [i for i in alert]

    def get_all_input_fields(self):
        wd = self.app.wd
        input_fields = wd.find_elements(By.XPATH, self.all_inputs)
        return [i.text for i in input_fields]

#####################  Dropdown ##########################
    def open_dropdown_menu(self, field_label):
        wd = self.app.wd
        wd.find_element(By.XPATH, self.dropdown_arrow_by_field_name % field_label).click()

    def select_dropdown_option(self, option):
        wd = self.app.wd
        wd.find_element(By.XPATH, self.dropdown_option % option).click()

    def get_dropdown_value_by_field(self, field_label):
        wd = self.app.wd
        return wd.find_element(By.XPATH, self.dropdown_value_container_by_field_name % field_label).text

    def get_all_dropdown_menu_options(self):
        wd = self.app.wd
        all_options = wd.find_elements(By.XPATH, self.dropdown_all_options)
        return [i.text for i in all_options]


#####################  Alert Notification  ##########################


    def get_alert_content(self):
        wd = self.app.wd
        alert_list = wd.find_elements(By.XPATH, self.alert_body_components)
        return [i.text for i in alert_list]

