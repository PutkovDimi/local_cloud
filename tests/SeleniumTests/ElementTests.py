import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest


@pytest.allure.feature("Testing of displaying elements")
class ElementTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    @pytest.allure.story("Display sign in form")
    def test_sign_in_displayed(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        elem = driver.find_element_by_xpath()