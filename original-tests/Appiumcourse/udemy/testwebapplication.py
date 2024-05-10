from appium import webdriver
from appium.options.common import AppiumOptions
import time

options = AppiumOptions()
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "ZY22KJKL8C")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.android.chrome")
options.set_capability("appActivity", "com.google.android.apps.chrome.Main")
options.set_capability("noReset", True)
options.set_capability("autoGrantPermissions", True)

# Ensure the Appium server is running on the correct port (4723 is the default)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
driver.implicitly_wait(10)

# Navigate to Google using Chrome's deep link
driver.execute_script("mobile: deepLink", {"url": "http://www.google.com", "package": "com.android.chrome"})
time.sleep(2)
print("Navigation successful")
time.sleep(5)
driver.quit()