import pytest


def get_data():
    return [
        ("ashok@gmail.com","ashok123"),
        ("ashok1@gmail.com","ashok1234"),
        ("ashok2@gmail.com","ashok1235"),
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
    print(username,password)
