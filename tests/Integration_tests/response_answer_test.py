import requests
import unittest
import pytest

URL_FORM = "http://127.0.0.1:5000/"


@pytest.allure.feature("Integration test")
class FormTest(unittest.TestCase):

    @pytest.allure.story("Test of response code")
    def test_get_200_response_code(self):
        try:
            r = requests.get(URL_FORM)
        except Exception:
            assert False
        else:
            assert r.status_code == 200
