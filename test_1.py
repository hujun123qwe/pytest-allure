"""
@time 2019/1/20
@autor jihong
"""

import pytest

#this paramter is defined in someclass
myname="hujun"


@pytest.mark("可以使用pytest的mark特性标记")
def test_username(username):
    assert username == myname
