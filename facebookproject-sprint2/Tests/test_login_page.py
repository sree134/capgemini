import datetime
import time

import pytest
from selenium.webdriver.support.select import Select

from Library.excel_lib import ReadExcel
from Library.config import Config
from POM.login_page import Loginpage


class TestLoginPage:
    """ contains the test scripts for the above automation scripts"""

    read_xl = ReadExcel()
    data = read_xl.read_testdata(Config.FACEBOOK_DATA_SHEET)

    @pytest.mark.parametrize("f_name,l_name,email,conf_email,pwd", data)
    def test_registration(self, init_driver, f_name, l_name, email, conf_email, pwd):

        global driver
        try:
            driver = init_driver
            lp = Loginpage(driver)
            lp = Loginpage(init_driver)
            lp.enter_firstname(f_name)
            lp.enter_lastname(l_name)
            lp.enter_mail_id(email)
            lp.enter_confirm_mail_id(conf_email)
            lp.enter_reg_pwd(pwd)
            lp.enter_day()
            lp.enter_month()
            lp.enter_year()
            lp.clickon_female_radio_button()
            lp.clickon_signup()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOTS_PATH + name)
            raise err_msg
