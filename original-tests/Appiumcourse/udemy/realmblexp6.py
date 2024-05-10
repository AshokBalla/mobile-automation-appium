import time
 
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
desired_caps['appActivity'] = '.Launcher'
desired_caps['noReset'] = True
desired_caps['automationName'] = 'UiAutomator2'
 
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',  options=capabilities_options)
driver.implicitly_wait(10)
 
driver.find_elements(By.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
 
elements = driver.find_elements(By.ID,'com.mobeta.android.demodslv:id/drag_handle')
 
actions = ActionChains(driver)
actions.click_and_hold(elements[0])
actions.move_to_element(elements[3])
actions.release(elements[3])
actions.perform()
 
time.sleep(2)
driver.quit()