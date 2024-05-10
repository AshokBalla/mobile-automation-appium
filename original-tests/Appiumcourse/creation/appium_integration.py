import pytest


def get_data():
    return [
        ("ashok@gmail.com","ashok123"),
        ("ashok1@gmail.com","ashok1234"),
        ("ashok2@gmail.com","ashok1235"),
    ]


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

def teardown_function():
    appium_service.stop()

@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
    print(username,password)
