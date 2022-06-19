#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: zy7y
@file: conftest.py
@ide: PyCharm
@time: 2020/12/8
@desc:
"""

import pytest


from tools.read_file import ReadFile



#不使用数据清洗 请把 下面代码解除注释 上面的get_db函数注释



@pytest.fixture(params=ReadFile.read_testcase())
def cases(request):
    """用例数据，测试方法参数入参该方法名 cases即可，实现同样的参数化
    目前来看相较于@pytest.mark.parametrize 更简洁。
    """
    return request.param