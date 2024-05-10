import pytest


@pytest.mark.functional
def test_login():
    print("Login successful")

@pytest.mark.regression
def test_reg():
    print("Registration successful")

@pytest.mark.functional
def test_email():
    print("Email successful")   

@pytest.mark.skip
def test_skip():
    print("Skipping test")

#pytest test4.py -v
#single test run
#pytest test4.py -s -v -k login 
#loign not run
#pytest test4.py -s -v -k "not login"

#pytest test4.py -s -v -m "functional"

