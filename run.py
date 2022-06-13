#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: zy7y
@file: run.py
@ide: PyCharm
@time: 2020/12/16
@github: https://github.com/zy7y
@site: https://cnblogs.com/zy7y
@desc: 运行文件
"""
from test_data.conftest import pytest
from string import Template
import os
import shutil
from tools import logger
from tools.read_file import ReadFile



file_path = ReadFile.read_config('$.file_path')

def run():
    # if os.path.exists('report/'):
    #     shutil.rmtree(path='report/')
    #
    # # 解决 issues 句柄无效
    # logger.remove()
    # logger.add(file_path['log'], enqueue=True, encoding='utf-8')
    # pytest.main(
    #     args=[
    #         'test_data/test_data.py',
    #         f'--alluredir={file_path["report"]}/data'])
    # logger.info(f'--alluredir={file_path["report"]}/data')
    # os.system(
    #     f'allure generate {file_path["report"]}data -o {file_path["report"]}html --clean')
    # logger.success('报告已生成')
    # a = ReadFile.read_testcase()
    pytest.main(args=['test_data/test_data.py'])


if __name__ == '__main__':
    run()

