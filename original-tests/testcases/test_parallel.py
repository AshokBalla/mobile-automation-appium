import unittest
import threading
import os
import time
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from concurrent.futures import ThreadPoolExecutor

# Global variables for tracking test results across threads
test_results = {}
lock = threading.Lock()

class AppiumTest(unittest.TestCase):
    """Base test class for running parallel tests on multiple devices"""
    
    def __init__(self, methodName='runTest', driver=None, device_id=None):
        super().__init__(methodName)
        self.driver = driver
        self.device_id = device_id
    
    def tearDown(self):
        # Note: We don't quit the driver here because it's managed by run_test
        pass
    
    def test_enter_value(self):
        """Test clicking on EnterValue button and entering a value"""
        try:
            if not self.driver:
                raise Exception("WebDriver is not initialized")
                
            print(f"[{self.device_id}] Starting test_enter_value")
            
            # 1. Find and click on the Enter Value button
            self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()
            print(f"[{self.device_id}] Clicked EnterValue button")
            
            # 2. Enter a test value in the input field
            input_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
            test_value = f"Test from {self.device_id}"
            input_field.send_keys(test_value)
            print(f"[{self.device_id}] Entered text: {test_value}")
            
            # 3. Take a screenshot to verify the input
            self.driver.save_screenshot(f"device_{self.device_id}_input.png")
            print(f"[{self.device_id}] Saved input screenshot")
            
            # 4. Click submit button
            submit_btn = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
            submit_btn.click()
            print(f"[{self.device_id}] Clicked submit button")
            
            # 5. Verify result
            time.sleep(1)  # Small wait for result screen
            result_text = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1").text
            print(f"[{self.device_id}] Result text: {result_text}")
            
            self.assertEqual(result_text, test_value, "Result text should match input")
            
            # 6. Take a screenshot of the result
            self.driver.save_screenshot(f"device_{self.device_id}_result.png")
            print(f"[{self.device_id}] Saved result screenshot")
            
            # Record test success
            with lock:
                test_results[self.device_id] = "PASS"
            
        except Exception as e:
            # Take screenshot on failure
            if self.driver:
                try:
                    self.driver.save_screenshot(f"device_{self.device_id}_error.png")
                    print(f"[{self.device_id}] Saved error screenshot")
                except:
                    pass
            
            # Record test failure
            with lock:
                test_results[self.device_id] = f"FAIL: {str(e)}"
            
            # Re-raise the exception for the test framework
            raise


def run_test(device_config):
    """Run the test on a specific device with the provided configuration"""
    driver = None
    device_id = device_config["deviceName"]
    
    try:
        # Extract device information
        port = device_config["port"]
        system_port = device_config["systemPort"]
        
        print(f"Starting test on device: {device_id} (Appium port: {port})")
        
        # Set up device capabilities
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.device_name = device_id
        capabilities.set_capability("appPackage", "com.code2lead.kwad")
        capabilities.set_capability("appActivity", "com.code2lead.kwad.MainActivity")
        capabilities.automation_name = "UiAutomator2"
        capabilities.set_capability("systemPort", system_port)
        
        # Create the driver
        driver = webdriver.Remote(f'http://localhost:{port}/wd/hub', options=capabilities)
        driver.implicitly_wait(10)
        
        # Create and run test
        suite = unittest.TestSuite()
        test = AppiumTest("test_enter_value", driver=driver, device_id=device_id)
        suite.addTest(test)
        
        # Run the test
        result = unittest.TextTestRunner().run(suite)
        
        # Log the result
        if result.wasSuccessful():
            print(f"Test on device {device_id} PASSED")
        else:
            print(f"Test on device {device_id} FAILED")
        
    except Exception as e:
        print(f"Error setting up/running test for device {device_id}: {e}")
        with lock:
            test_results[device_id] = f"SETUP FAIL: {str(e)}"
    
    finally:
        # Always quit the driver
        if driver:
            driver.quit()


def main():
    """Main function to run tests in parallel on multiple devices"""
    # Define device configurations - update these with your actual device IDs
    devices = [
        {
            "deviceName": "emulator-5554",  # First emulator
            "port": 4723,                  # First Appium server port
            "systemPort": 8200             # First system port
        },
        {
            "deviceName": "emulator-5556",  # Second emulator (if available)
            "port": 4724,                  # Second Appium server port
            "systemPort": 8201             # Second system port
        }
    ]
    
    # Check which devices are actually available
    available_devices = []
    try:
        # Get connected devices
        import subprocess
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        connected_devices = result.stdout.strip().split('\n')[1:]
        connected_device_ids = [device.split('\t')[0] for device in connected_devices if device and '\t' in device]
        
        print(f"Connected devices: {connected_device_ids}")
        
        for device in devices:
            if device["deviceName"] in connected_device_ids:
                available_devices.append(device)
        
        if not available_devices:
            print("No configured devices are connected. Please check your device connections.")
            return
        
    except Exception as e:
        print(f"Error checking available devices: {e}")
        return
    
    print(f"Found {len(available_devices)} available device(s): {[d['deviceName'] for d in available_devices]}")
    
    # Run tests in parallel using a thread pool
    with ThreadPoolExecutor(max_workers=len(available_devices)) as executor:
        executor.map(run_test, available_devices)
    
    # Print final results
    print("\n==== TEST RESULTS ====")
    for device_id, result in test_results.items():
        print(f"Device {device_id}: {result}")


if __name__ == "__main__":
    main()
    
# To run:
# 1. Make sure you have multiple devices/emulators connected
# 2. Start multiple Appium server instances on different ports (e.g., 4723, 4724)
# 3. Run this script: python3 test_parallel.py
