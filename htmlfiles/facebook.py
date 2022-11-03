import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
path = r"C:\Users\sreen\PycharmProjects\Selenium_project\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
url = r"https://www.facebook.com/r.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("name","firstname").send_keys("varalakshmi")
time.sleep(2)
driver.find_element("name","lastname").send_keys("dande")
time.sleep(2)
driver.find_element("name","reg_email__").send_keys("dandevaralakshmi410@gmail.com")
time.sleep(2)
driver.find_element("name","reg_email_confirmation__").send_keys("dandevaralakshmi410@gmail.com")
time.sleep(2)
driver.find_element("name","reg_passwd__").send_keys("VaraLak@410")
time.sleep(2)
day = driver.find_element("id","day")
obj = Select(day)
obj.select_by_visible_text("30")

month = driver.find_element("name","birthday_month")
obj = Select(month)
time.sleep(2)
obj.select_by_value("10")

year = driver.find_element("id","year")
obj = Select(year)
obj.select_by_visible_text("2000")
time.sleep(2)
driver.find_element("xpath", '(//input[@class="_8esa"])[1]').click()
time.sleep(2)
driver.find_element("xpath",'(//button[text()="Sign Up"])[1]').click()
time.sleep(30)
driver.find_element("xpath",'//button[@type="submit"]').click()





