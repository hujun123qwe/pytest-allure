"""
@time 2019/1/20
@autor jihong
"""

import pytest
import allure

@allure.feature('test_module_01')
def test_case_01():
    assert 1, '测试用例1'

@allure.feature('test_module_02')
def test_case_02():
    assert 2, '测试用例2'

