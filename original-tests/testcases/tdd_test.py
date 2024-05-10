import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

class EnterValueTests(unittest.TestCase):
    """Test class for the EnterValue functionality in the KWAD app"""
    
    @classmethod
    def setUpClass(cls):
        """Set up the test class - executed once before all tests"""
        print("Setting up test class...")
        
        # Set up capabilities
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.platform_version = "15"
        capabilities.device_name = "emulator-5554"
        capabilities.set_capability("appPackage", "com.code2lead.kwad")
        capabilities.set_capability("appActivity", "com.code2lead.kwad.MainActivity")
        capabilities.automation_name = "UiAutomator2"
        
        # Connect to Appium server - using the /wd/hub endpoint for better compatibility
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=capabilities)
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests have run"""
        print("Tearing down test class...")
        if cls.driver:
            cls.driver.quit()
    
    def setUp(self):
        """Set up each test case - return to home screen before each test"""
        print(f"Starting test: {self._testMethodName}")
        # Try to go back to home if not already there
        try:
            # Check if we're on the home screen by looking for the EnterValue button
            if not self.is_element_present(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"):
                # Press back until we get to the home screen or timeout
                for _ in range(3):  # Try max 3 times
                    self.driver.press_keycode(4)  # Android back button
                    time.sleep(1)
                    if self.is_element_present(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"):
                        break
        except Exception as e:
            print(f"Exception in setUp: {e}")
    
    def tearDown(self):
        """Clean up after each test case"""
        print(f"Finished test: {self._testMethodName}")
    
    def is_element_present(self, by, value):
        """Helper method to check if an element is present"""
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False
            
    def test_enter_value_navigation(self):
        """Test that clicking the EnterValue button navigates to the EnterValue screen"""
        # 1. Click on EnterValue button
        enter_value_btn = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
        enter_value_btn.click()
        
        # 2. Verify that we navigated to the right screen by checking for the input field
        input_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
        self.assertTrue(input_field.is_displayed(), "Input field should be displayed after navigation")
        
        # 3. Check that the screen has the correct title
        screen_title = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Enter some Value']")
        self.assertTrue(screen_title.is_displayed(), "Screen title should be visible")
    
    def test_enter_value_input(self):
        """Test entering a value and submitting it"""
        # 1. Click on EnterValue button
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()
        
        # 2. Enter a test value
        test_value = "TDD Test Value"
        input_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
        input_field.clear()
        input_field.send_keys(test_value)
        
        # 3. Click the submit button
        submit_btn = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
        submit_btn.click()
        
        # 4. Verify the result screen shows our entered value
        result_text = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1").text
        # The actual app returns just the text value without the "You have entered : " prefix
        self.assertEqual(result_text, test_value, "Result text should match our input")
    
    def test_enter_value_empty_input(self):
        """Test behavior when submitting with empty input"""
        # 1. Click on EnterValue button
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()
        
        # 2. Clear any existing text
        input_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
        input_field.clear()
        
        # 3. Click the submit button without entering text
        submit_btn = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
        submit_btn.click()
        
        # 4. Verify we're still on the same screen (no navigation happened)
        self.assertTrue(input_field.is_displayed(), "Should remain on input screen when submitting empty value")


if __name__ == "__main__":
    unittest.main()
#python3 tdd_test.py