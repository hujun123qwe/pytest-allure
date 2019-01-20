"""
@time 2019/1/20
@autor jihong
"""

import pytest

#this paramter is defined in someclass
myname="hujun"


def test_username(username):
    assert username == myname
