import re
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select


@given(u'Open the chrome browser enter the valid URL')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\sreen\PycharmProjects\Selenium_project\drivers\chromedriver.exe")
    context.driver.get("https://www.facebook.com/signup")
    context.driver.implicitly_wait(5)


@when(u'enter the first name "{f_name}"')
def step_impl(context,f_name):
    context.driver.find_element("name","firstname").send_keys(f_name)
    time.sleep(2)


@when(u'enter the last name "{l_name}"')
def step_impl(context,l_name):
    context.driver.find_element("name","lastname").send_keys(l_name)
    time.sleep(2)

@when(u'enter the email_id "{email_id}"')
def step_impl(context,email_id):


    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, email_id)
    assert result, "invalid email_id"
    context.driver.find_element("name", "reg_email__").send_keys(email_id)

    time.sleep(2)


@when(u're_enter the conform_emailid "{conform_emailid}"')
def step_impl(context,conform_emailid):
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern,conform_emailid )
    assert result, "invalid conform_emailid"
    context.driver.find_element("name", "reg_email_confirmation__").send_keys(conform_emailid)

    time.sleep(2)

@when(u'enter the pwd "{pwd}"')
def step_impl(context,pwd):
    context.driver.find_element("name", "reg_passwd__").send_keys(pwd)
    time.sleep(2)


@when(u'click the day')
def step_impl(context):
    list_box1 = context.driver.find_element("id","day")
    s_obj = Select(list_box1)
    s_obj.select_by_visible_text("30")
    time.sleep(3)

@when(u'click the month')
def step_impl(context):
    list_box2 = context. driver.find_element("name","birthday_month")
    s_obj = Select(list_box2)
    s_obj.select_by_visible_text("Oct")
    time.sleep(3)

@when(u'click the year')
def step_impl(context):
    list_box3 = context.driver.find_element("id","year")
    s_obj = Select(list_box3)
    s_obj.select_by_visible_text("2000")
    time.sleep(3)


@when(u'click on the gender female radio button')
def step_impl(context):
    context.driver.find_element("xpath",'(//input[@type="radio"])[1]').click()
    time.sleep(2)

@when(u'click on the Signup button')
def step_impl(context):
    context.driver.find_element("xpath",'(//button[@type="submit"]) [1]').click()
    time.sleep(2)

@then(u'close chrome browser')
def step_impl(context):
    context.driver.close()