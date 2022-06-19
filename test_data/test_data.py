import pytest
from api.base_request import Client
from tools.read_file import ReadFile


def test_main(cases):   # 不使用数据库功能
    # 发送请求
    response = Client.action(cases)

# if __name__ == '__main__':
#     pytest.main(['-s','test_data.py'])

