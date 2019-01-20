"""
@time 2019/1/20
@autor jihong
"""

import pytest
import allure

@allure.feature('test_module_01')
@pytest.mark.skipif('2+2!=5', reason="这个测试被跳过了，因为前面的条件不成立")
def test_case_01():
    assert 1, '测试用例1'

@allure.feature('test_module_02')
@pytest.mark.xfail(condition=lambda:True, reason="使用xfail来期望错误，可以设置错误几个就停止")
def test_case_02():
    assert 2, '测试用例2'

