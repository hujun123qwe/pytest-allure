"""
@time 2019/1/20
@autor jihong
"""

import os
import configparser


PATH = os.path.split(os.path.realpath(__file__))[0]
# ('D:\\hujun\\project1\\conf', 'config.py')

AbstractPath = os.path.realpath(__file__)
# D:\hujun\project1\conf\config.py


class ConfigHost(object):
    def __init__(self):
        config_host = configparser.ConfigParser()
        config_host.read(PATH+'/config.ini', encoding='utf-8')
        self.host = config_host['host']

    def get_host_conf(self):
        return self.host

#当直接运行此文件时使用
if __name__ == '__main__':
    host = ConfigHost()
    tmp = host.get_host_conf()
    for k in tmp:
        print(k, tmp[k])
