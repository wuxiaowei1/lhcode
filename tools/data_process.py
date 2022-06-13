from tools import allure_step_no
from tools.read_file import ReadFile

class DataProcess:
    extra_pool = {}

    @classmethod
    def handle_path(cls, path_str:str, env:str):
        url = ReadFile.read_config(f'$.server.{env}') + path_str
        allure_step_no(f'请求地址:{url}')
        return url

