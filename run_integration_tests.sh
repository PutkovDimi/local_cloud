#!/usr/bin/env bash

py.test tests/Integration_tests/response_answer_test.py --alluredir ./tests/reports/response_report/
allure generate tests/reports/response_report --clean