"""
@time 2019/1/20
pytest配置文件，有fixtures手脚架，有mark标记
@autor jihong
"""

import pytest


@pytest.fixture()
def username():
    return "hujun"


