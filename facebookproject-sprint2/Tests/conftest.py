import pytest
from Library.config import Config
from selenium import webdriver


@pytest.fixture(params=["Chrome"]) #, "firefox", "edge"
def init_driver(request):
    """ consists of the setup and tear down methods that is executed before and after each testcases"""
    global driver
    browser = request.param

    if browser.lower() == "chrome":
        # chrome_path = r"C:\Users\sreen\PycharmProjects\facebookproject-sprint2\drivers\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH)

    #
    # elif browser.lower() == "firefox":
    #     # firefox_path = r"C:\Users\sreen\PycharmProjects\facebookproject-sprint2\drivers\geckodriver.exe"
    #     driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH)
    #
    # else:
    #     # edge_path = r"C:\Users\sreen\PycharmProjects\facebookproject-sprint2\drivers\msedgedriver.exe"
    #     driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.close()
