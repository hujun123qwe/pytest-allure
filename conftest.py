"""
@time 2019/1/20
pytest配置文件，有fixtures手脚架，有mark标记
@autor jihong
"""

import pytest

#手脚架要先声明清楚
@pytest.fixture()
def username():
    return "hujun"


