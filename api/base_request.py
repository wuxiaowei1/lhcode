from requests import Session, request
from tools.read_file import ReadFile
from tools import allure_step, allure_title, logger, allure_step_no
from tools.data_process import DataProcess

class Transmission:
    PARAMS: str = "params"
    DATA: str = "data"
    JSON: str = "json"

class Client(Session):
    header = ReadFile.read_config('$.request_headers')
    def baes_request(self, url, method, parametric_key, header=None, data=None, file=None):
        if parametric_key == Transmission.PARAMS:
            extra_args = {Transmission.PARAMS: data}
        elif parametric_key == Transmission.DATA:
            extra_args = {Transmission.DATA: data}
        elif parametric_key == Transmission.JSON:
            extra_args = {Transmission.JSON: data}
        else:
            raise ValueError("可选关键字为params, json, data")
        res = request(method=method, url=url, headers=header, params=data)
        response = res.json()
        logger.info(
            f"\n请求地址:{res.url}\n请求方法:{method}\n请求头:{header}\n请求参数:{data}\n\n响应数据:{response}"
        )
        allure_step_no(f"响应耗时(s): {res.elapsed.total_seconds()}")
        allure_step("响应结果", response)
        return response

    def action(self, case: list, env: str = "dev") :
        """处理case数据，转换成可用数据发送请求
        :param case: 读取出来的每一行用例内容，可进行解包
        :param env: 环境名称 默认使用config.yaml server下的 dev 后面的基准地址
        return: 响应结果， 预期结果
        """
        (
            _,
            case_title,
            header,
            path,
            method,
            parametric_key,
            file_obj,
            data,
            extra,
            sql,
            expect,
        ) = case
        logger.debug(
            f"用例进行处理前数据: \n 接口路径: {path} \n 请求参数: {data} \n  提取参数: {extra} \n 后置sql: {sql} \n 预期结果: {expect} \n "
        )
        # allure报告 用例标题
        allure_title(case_title)
        # 处理url、header、data、的前置方法
        url = DataProcess.handle_path(path, env)
        headers = self.header
        data = data
        allure_step("请求数据", data)
        # 发送请求
        response = self.baes_request(url, method, parametric_key, headers, data)
        return response

# if __name__ == '__main__':
#      Client().action()