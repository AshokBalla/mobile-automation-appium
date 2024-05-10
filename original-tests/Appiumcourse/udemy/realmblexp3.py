class ScrollUtil:
 
    @staticmethod
    def scrollToTextByAndroidUIAutomator(text,driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()
 
 
    @staticmethod
    def swipeUp(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 200)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()
 
    @staticmethod
    def swipeDown(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 500)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 800)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()
 
    @staticmethod
    def swipeLeft(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()
 
    @staticmethod
    def swipeRight(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()
