from configparser import ConfigParser


config = ConfigParser()
config.read("../utilities/config.ini")
print(config.get("basic info ", "test_url"))
print(config.get("basic info ", "test_username"))
print(config.get("basic info ", "test_password"))
print(config.get("basic info ", "implicit.wait"))
print(config.get("basic info ", "explicit.wait"))
print(config.get("test_data", "test_data_file"))
print(config.get("locator", "username_locator"))
print(config.get("locator", "password_locator"))
print(config.get("locator", "login_button_locator"))



def read_config(section, key):
    config = ConfigParser()
    config.read("../utilities/config.ini")
    return config.get(section, key)

print(read_config("basic info ", "test_url"))
print(read_config("basic info ", "test_username"))
print(read_config("basic info ", "test_password"))


#python3 configreader.py