import time
 
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.samsung.android.dialer'
desired_caps['appActivity'] = '.DialtactsActivity'
desired_caps['automationName'] = 'UiAutomator2'
 
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',  options=capabilities_options)
driver.implicitly_wait(10)
 
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))').click()
 
time.sleep(2)
driver.quit()