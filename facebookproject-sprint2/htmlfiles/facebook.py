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
driver.find_element("xpath",'//select[@id="day"]//option[10]').click()
driver.find_element("xpath",'//select[@id="month"]//option[11]').click()
driver.find_element("xpath",'//select[@id="year"]//option[20]').click()
driver.find_element("xpath", '(//input[@type="radio"])[1]').click()
time.sleep(2)
driver.find_element("xpath",'(//button[text()="Sign Up"])[1]').click()
time.sleep(30)
driver.find_element("xpath",'(//button[@type="submit"])[1]').click()





