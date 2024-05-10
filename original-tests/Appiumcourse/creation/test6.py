import pytest


def test_valid_title():
    expected_title = "Gmail.com"
    actual_title = "Gmail.com"
    title = "this is gmail website"

    # if expected_title == actual_title:
    #     print("Title is pass")
    # else:
    #     print("Test case failed")
    
    # Add proper assertion
    print("Beginning of the test")
    assert expected_title == actual_title, f"Expected '{expected_title}' but got '{actual_title}'"
    assert "Gmail" in title , "Gmail is does not exist in the title"
    assert False, "This is a failed test"
    print("End of the test")



#pip install pytest-soft-assertions
#pip install pytest-html

