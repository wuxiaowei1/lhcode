#coding=UTF8
"""
    @Author : chenWanYue
    @Time   : 8/30/21 6:49 PM
    @Desc   :
"""
import jwt
import datetime
import json

# json.loads函数的使用，将字符串转化为字典
# json_info = '{"total_cost"："$.data.content[0].total_cost"}'
# dict1 = json.loads(json_info)
# print("json_info的类型："+str(type(json_info)))
# print("通过json.dumps()函数处理：")
# print("dict1的类型："+str(type(dict1)))
#
def create_token(db_wwu_id, db_wwu_name):
    """
    生成平台访问token
    :author: chenWanYue
    :param db_wwu_id:
    :param db_wwu_name:
    :return:
    """
    # 测试 #9ue0xwJQtW&i&vCSldXO5rEP9Kc&qBy
    # 生产 1np1iWjod#HZmwUIaJOr4czT8gtCRd9o
    payload = {
        "id": db_wwu_id,
        "name": db_wwu_name,
        "type": "AccountToken",
        "exp": int((datetime.datetime.now() + datetime.timedelta(hours=2400)).timestamp())
    }
    token = jwt.encode(payload=payload, key="#9ue0xwJQtW&i&vCSldXO5rEP9Kc&qBy", algorithm="HS256")
    # token = jwt.encode(payload=payload, key="1np1iWjod#HZmwUIaJOr4czT8gtCRd9o", algorithm="HS256")
    print(token)


def run(user_id, name):
    create_token(user_id, name)

if __name__ == '__main__':
    # run(789, '周克琼')
    run(1760, '刘茂平')
