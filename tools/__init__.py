import json

from jsonpath import jsonpath
from loguru import logger
import allure

def extractor(obj: dict, expr: str = '.'):
    try:
        result = jsonpath(obj, expr)[0]
    except Exception as e:
        result = expr
    return result

def allure_title(title: str):
    """allure中显示的用例标题"""
    allure.dynamic.title(title)

def allure_step(step: str, var: str):
    """
    :param step: 步骤及附件名称
    :param var: 附件内容
    """
    with allure.step(step):
        allure.attach(
            json.dumps(
                var,
                ensure_ascii=False,
                indent=4),
            step,
            allure.attachment_type.JSON)

def allure_step_no(step: str):
    """
    无附件的操作步骤
    :param step: 步骤名称
    :return:
    """
    with allure.step(step):
        pass
