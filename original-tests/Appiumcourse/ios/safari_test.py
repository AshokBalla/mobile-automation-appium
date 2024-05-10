import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options

# Configure Safari Driver options
safari_options = Options()
safari_options.add_argument("--allow-file-access-from-files")
safari_options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")

# Initialize the Safari driver directly via Selenium (bypassing Appium)
try:
    print("Launching Safari on macOS...")
    driver = webdriver.Safari(options=safari_options)
    
    # Set window size
    driver.set_window_size(390, 844)  # iPhone dimensions
    
    # Navigate to a website
    print("Navigating to example.com...")
    driver.get('https://www.example.com')
    
    # Wait for page to load
    time.sleep(2)
    
    # Get and print page title
    title = driver.title
    print(f"Page title: {title}")
    
    # Take a screenshot
    driver.save_screenshot('safari_desktop_screenshot.png')
    print("Screenshot saved as safari_desktop_screenshot.png")
    
    # Get some text from the page
    main_text = driver.find_element(By.TAG_NAME, 'h1').text
    print(f"Main heading: {main_text}")
    
    # Navigate to another page
    print("Navigating to google.com...")
    driver.get('https://www.google.com')
    
    # Wait for page to load
    time.sleep(2)
    
    # Take another screenshot
    driver.save_screenshot('google_screenshot.png')
    print("Screenshot saved as google_screenshot.png")
    
    # Wait before closing
    time.sleep(3)
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    # Close the driver
    if 'driver' in locals():
        print("Closing Safari...")
        driver.quit()
        print("Session ended")

print("Test completed") 