import pytest
import os
import allure
@allure.step("第一步")
def step_1():
    step_2()
    print("打开浏览器")
@allure.step("第二步")
def step_2():
    step_3()
    print("输入URL")
@allure.step("第三步")
def step_3():
    print("登入成功")
@allure.step("第四步")
def test_login():
    step_1()

if __name__ == '__main__':
    pytest.main(['lh_study.py',  '--alluredir', 'lhcode/report/data'])
    os.system('allure generate lhcode/report/data -o lhcode/report/html --clean')
    os.system('allure serve lhcode/report/data')