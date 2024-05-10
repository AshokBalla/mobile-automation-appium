# from appium import webdriver
# from appium.options.common.base import AppiumOptions
# import time

# options = AppiumOptions()
# options.set_capability('deviceName', 'Android Emulator')
# options.set_capability('platformName', 'Android')
# options.set_capability('platformVersion', '15')

# options.set_capability('app', '/Users/ashokballa/Downloads/Android_Demo_App.apk')
# options.set_capability('automationName', 'UiAutomator2')
# options.set_capability('ensureWebviewsHavePages', True)

# driver = webdriver.Remote('http://localhost:4725/wd/hub', options=options)
# driver.implicitly_wait(10)
# driver.get('http://www.google.com')

# time.sleep(5)
# driver.quit()

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

options = AppiumOptions()
options.set_capability('deviceName', 'sdk_gphone64_arm64')
options.set_capability('platformName', 'Android')
options.set_capability('platformVersion', '15')
options.set_capability('app', '/Users/ashokballa/Downloads/Android_Demo_App.apk')
options.set_capability('automationName', 'UiAutomator2')
options.set_capability('ensureWebviewsHavePages', True)
options.set_capability('nativeWebScreenshot', True)
options.set_capability('newCommandTimeout', 3600)
options.set_capability('connectHardwareKeyboard', True)

driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
driver.implicitly_wait(10)

# Perform a simple action like clicking on the EnterValue button
enter_value_element = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/EnterValue")
enter_value_element.click()

time.sleep(5)
driver.quit()  # Added driver.quit() to properly close the session



# To run the test, use the following command:
#python3 test1.py