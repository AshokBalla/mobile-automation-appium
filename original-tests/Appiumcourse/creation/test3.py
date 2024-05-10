import pytest

@pytest.fixture(scope="module")
def setup_():
    print("Creating DB connection")
    yield
    print("Closing DB connection")

@pytest.fixture(scope="function")
def before():
    print("launching browser")
    yield

    print("Quitting browser")



# def test_login(before):
#     print("Entering login credentials")
   
# def test_reg(before):
#     print("Registration successful")

@pytest.mark.usefixtures("setup_","before")
def test_login():
    print("Entering login credentials")
   
@pytest.mark.usefixtures("setup_","before")
def test_reg():
    print("Registration successful")