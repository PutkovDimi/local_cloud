#!/usr/bin/env bash

py.test tests/SeleniumTests/ElementTests.py --alluredir ./tests/reports/selenium_report/
allure generate tests/reports/selenium_report --clean