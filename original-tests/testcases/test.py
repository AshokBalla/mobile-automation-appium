from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

print("Setting up capabilities...")
capabilities = UiAutomator2Options()
capabilities.platform_name = "Android"
capabilities.platform_version = "15"
capabilities.device_name = "emulator-5554"
# Instead of using the APK file, use appPackage and appActivity
capabilities.set_capability("appPackage", "com.code2lead.kwad")
capabilities.set_capability("appActivity", "com.code2lead.kwad.MainActivity")
capabilities.automation_name = "UiAutomator2"

print("Connecting to Appium server...")
# For Appium 2.x, the /wd/hub prefix is no longer used
driver = webdriver.Remote('http://localhost:4723', options=capabilities)
print("Connected successfully")

driver.implicitly_wait(10)
print("Finding element...")
driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()
print("Element clicked")

driver.quit()
print("Test completed successfully")

if __name__ == "__main__":
	pass