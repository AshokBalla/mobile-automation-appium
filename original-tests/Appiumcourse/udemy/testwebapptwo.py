from appium import webdriver
from appium.options.common.base import AppiumOptions
import time

options = AppiumOptions()
options.set_capability('deviceName', 'Android Emulator')
options.set_capability('platformName', 'Android')
options.set_capability('platformVersion', '15')
options.set_capability('browserName', 'Chrome')
options.set_capability('chromedriverExecutable', '/Users/ashokballa/Downloads/chromedriver_mac64/chromedriver')

driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
driver.implicitly_wait(10)
driver.get('http://www.google.com')

time.sleep(5)
driver.quit()