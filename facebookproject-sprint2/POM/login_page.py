import re
import time
from Library.excel_lib import ReadExcel
from Library.config import Config
from selenium.webdriver.support.select import Select


class Loginpage:
    """ consists of the automation script/ business logic of  Registration page of demo web shop"""
    read_xl = ReadExcel()
    login_locators = read_xl.read_locators(Config.FACEBOOK_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, f_name):
        locator = self.login_locators["enter_firstname"]
        self.driver.find_element(*locator).send_keys(f_name)

    def enter_lastname(self, l_name):
        locator = self.login_locators["enter_lastname"]
        self.driver.find_element(*locator).send_keys(l_name)

    def enter_mail_id(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"
        locator = self.login_locators["enter_mail_id"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_confirm_mail_id(self, conf_email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, conf_email)
        assert result, "invalid conf_email"
        locator = self.login_locators["enter_confirm_mail_id"]
        self.driver.find_element(*locator).send_keys(conf_email)

    def enter_reg_pwd(self, pwd):
        if isinstance(pwd, float):
            pwd = str(int(pwd))
        assert len(pwd) >= 6, "password should have atleast 6 characters"
        locator = self.login_locators["enter_reg_pwd"]
        self.driver.find_element(*locator).send_keys(pwd)
        return pwd
        time.sleep(2)

    def enter_day(self):
        locator = self.login_locators["enter_day"]
        self.driver.find_element(*locator).click()

    def enter_month(self):
        locator = self.login_locators["enter_month"]
        self.driver.find_element(*locator).click()

    def enter_year(self):
        locator = self.login_locators["enter_year"]
        self.driver.find_element(*locator).click()

    def clickon_female_radio_button(self):
        locator = self.login_locators["clickon_female_radio_button"]
        self.driver.find_element(*locator).click()

    def clickon_signup(self):
        locator_name, locator_value = self.login_locators["clickon_signup"]
        self.driver.find_element(locator_name, locator_value).click()
