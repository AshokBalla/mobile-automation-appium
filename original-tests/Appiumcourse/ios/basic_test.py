from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Setup desired capabilities
capabilities = {
    'platformName': 'iOS',
    'platformVersion': '18.2',
    'deviceName': 'iPhone 16 Pro Max',
    'udid': '232A3994-152F-44A3-8989-378900E65FC7',
    'automationName': 'XCUITest',
    'bundleId': 'com.apple.calculator'  # Using built-in Calculator app
}

print("Starting Appium test with capabilities:")
for key, value in capabilities.items():
    print(f"  {key}: {value}")

try:
    # Connect to the Appium server
    print("\nConnecting to Appium server...")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    print("Connected successfully!")
    
    # Wait for app to load
    driver.implicitly_wait(5)
    
    # Interact with calculator buttons
    print("\nPerforming calculator operations...")
    
    # Press 5
    five_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
    five_button.click()
    print("Pressed: 5")
    
    # Press +
    plus_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
    plus_button.click()
    print("Pressed: +")
    
    # Press 3
    three_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="3")
    three_button.click()
    print("Pressed: 3")
    
    # Press =
    equals_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
    equals_button.click()
    print("Pressed: =")
    
    # Get result
    result = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[1]").text
    print(f"\nCalculation result: {result}")
    
    # Take a screenshot
    driver.get_screenshot_as_file('calculator_screenshot.png')
    print("Screenshot saved as 'calculator_screenshot.png'")
    
    # Wait before closing
    time.sleep(3)
    
except Exception as e:
    print(f"\nERROR: {e}")

finally:
    # Quit driver
    if 'driver' in locals():
        print("\nClosing session...")
        driver.quit()
        print("Session ended") 