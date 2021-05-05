""" Test Cases """

import validators

def is_test_valid():
    """ Test case to see if the URL is a valid one """
    valid=validators.url()
    if valid==True:
        print("Valid")
    else:
        print("Invalid")

def test_html_to_html():
    """ Test case to look into HTML -> HTML """

def test_MD_to_html():
    """ Test case to look into MD -> HTML """

def test_RST_to_html():
    """ Test case to look into RST -> HTML """
