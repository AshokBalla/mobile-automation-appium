import pytest

def setup_module(module):
    print("Creating DB connection")

def teardown_module(module):
    print("Closing DB connection")

def setup_function(function):
    print("launching browser")

def teardown_function(function):
    print("Quitting browser")

def test_login():
    print("Login successful")

def test_reg():
    print("Registration successful")

#pytest test2.py -v
#python3 -m pytest test2.py -v