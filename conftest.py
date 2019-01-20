"""
@time 2019/1/20
pytest配置文件，有fixtures手脚架，有mark标记
@autor jihong
"""

import pytest
import allure

from conf.config import ConfigHost


#手脚架要先声明清楚
@pytest.fixture()
def username():
    return "hujun"

@pytest.fixture(scope='session', autouse='true')
def env():
    host_config = ConfigHost()
    host = host_config.get_host_conf()
    for k in host:
        allure.environment(k=host[k])




