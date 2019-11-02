import pytest
from selenium.webdriver import Chrome

def get_driver_instance():
    browser = pytest.config.option.type.lower()
    if browser == 'chrome':
        driver = Chrome("./browser-server/chromedriver.exe")
    elif browser == 'firefox':
        driver = Chrome("./browser-server/geckodriver.exe")
    else:
        print('Invalid Browser Option')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://localhost")
    return driver
