import time
 
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
 
from testcases.scroll_util import ScrollUtil
 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'flipboard.app'
desired_caps['appActivity'] = 'flipboard.activities.LaunchActivityAlias'
desired_caps['automationName'] = 'UiAutomator2'
 
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',  options=capabilities_options)
driver.implicitly_wait(10)
 
 
driver.find_element(AppiumBy.ID,'flipboard.app:id/first_launch_cover_continue').click()
 
driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[0].click()
driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[1].click()
driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[2].click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/topic_picker_continue_button').click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/account_login_buttons_skip').click()
time.sleep(2)
ScrollUtil.swipeUp(4,driver)
time.sleep(2)
ScrollUtil.swipeDown(4,driver)
time.sleep(2)
ScrollUtil.swipeLeft(2,driver)
time.sleep(2)
ScrollUtil.swipeRight(2,driver)
 
time.sleep(2)
driver.quit()