import time
 
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions
 
from testcases.scroll_util import ScrollUtil
 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = 'com.android.contacts.DialtactsContactsEntryActivity'
 
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
 
#ScrollUtil.scrollToTextByAndroidUIAutomator("Akash",driver)
#driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))').click()
# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
#
#
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)
 
# ScrollUtil.swipeUp(4,driver)
# ScrollUtil.swipeDown(4,driver)
 
elements = driver.find_elements_by_id('com.android.contacts:id/cliv_name_textview')
print(len(elements))
 
actions = TouchAction(driver)
#actions.tap(elements[2])
actions.long_press(elements[2])
actions.perform()
 
 
 
time.sleep(2)
driver.quit()