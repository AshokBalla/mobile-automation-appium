import pytest

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestAndroid:
	
	@pytest.fixture()
	def driver(self):
		options = AppiumOptions()
		options.load_capabilities({
			"platformName": "Android",
			"appium:platformVersion": "15",
			"appium:deviceName": "sdk_gphone64_arm64",
			"appium:automationName": "UiAutomator2",
			"appium:app": "/Users/ashokballa/Downloads/Android_Demo_App.apk",
			"appium:ensureWebviewsHavePages": True,
			"appium:nativeWebScreenshot": True,
			"appium:newCommandTimeout": 3600,
			"appium:connectHardwareKeyboard": True


		})

		driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
		driver.implicitly_wait(10)
		yield driver
		driver.quit()

	def test_click(self, driver):
		wait = WebDriverWait(driver, 20)
		
		enter_value_element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")))
		enter_value_element.click()
		
		

if __name__ == "__main__":
	pytest.main()

# To run the test, use the following command:
#python3 -m pytest test.py -v
#pytest test.py --html=report.html