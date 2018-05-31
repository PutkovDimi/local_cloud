import unittest
from selenium import webdriver
import pytest
import random, string
import os

TEST_FILE = "/tests/SeleniumTests/TestFile.txt"


def randomword(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.allure.feature("Testing of displaying elements")
class ElementTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    @pytest.allure.story("Display have access alert")
    @pytest.allure.step("Display have access alert")
    def test_sign_in_displayed(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        elem = driver.find_element_by_xpath("//div[@class='alert alert-warning']")
        assert elem.text == '×\nPlease log in to access this page.'

    @pytest.allure.story("sign up successfully")
    @pytest.allure.step("sign up successfully")
    def test_sign_up(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/sign_up")
        elem = driver.find_element_by_xpath("//input[@id='email']")
        elem.send_keys(randomword())
        elem = driver.find_element_by_xpath("//input[@id='password']")
        elem.send_keys(randomword())
        elem = driver.find_element_by_xpath("//input[@id='submit']")
        elem.click()
        assert driver.current_url == 'http://127.0.0.1:5000/'

    @pytest.allure.story("Upload files ability")
    @pytest.allure.step("Upload files ability")
    def test_upload_files(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        elem = driver.find_element_by_xpath("//input[@id='upload-file']")
        elem.send_keys(os.getcwd() + TEST_FILE)
        elem.find_element_by_xpath("//button[@id='submit-button']")
        elem.click()
        elem = driver.find_element_by_xpath("//div[@class='alert alert-warning']")
        assert elem.text == 'Your file was saved successfully'


    def tearDown(self):
        self.driver.close()
