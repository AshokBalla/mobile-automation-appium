import time
from appium import webdriver
from appium.options.ios import XCUITestOptions

# Create an XCUITestOptions instance
options = XCUITestOptions()
options.platform_name = 'iOS'
options.platform_version = '18.2'
options.device_name = 'iPhone 16 Pro Max'
options.udid = '232A3994-152F-44A3-8989-378900E65FC7'
options.bundle_id = 'com.apple.mobilesafari'

# Additional capabilities
options.set_capability("showXcodeLog", True)
options.set_capability("useNewWDA", False)
options.set_capability("noReset", True)

print(f"Starting test with iOS {options.platform_version} on {options.device_name}")
print(f"UDID: {options.udid}")
print(f"Connecting to Appium server...")

try:
    # Connect to Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    
    # Set implicit wait
    driver.implicitly_wait(10)
    print("Connected successfully! Launching Safari...")
    
    # Navigate to a website
    print("Navigating to example.com...")
    driver.get('https://www.example.com')
    print("Page loaded")
    
    # Wait for the page to load
    time.sleep(5)
    
    # Take a screenshot
    driver.get_screenshot_as_file('mobile_safari_screenshot.png')
    print("Screenshot saved")

except Exception as e:
    print(f"Error occurred: {e}")
    
finally:
    # Quit driver if it exists
    if 'driver' in locals():
        print("Test complete. Closing session...")
        driver.quit()
        print("Session ended")