from requests import Session
from tools.read_file import ReadFile



class Client(Session):

    header = ReadFile.read_config('$.request_headers')
    base_url = str(ReadFile.read_config('$.server')["test"])


    def baes_request(self, url, methon, header=None, data=None):
        res = self.request(method=methon, url = url, headers= header, data=data)
        response = res.json()
    def action(self):
        url = self.base_url + "123"
        data = {
            "data":1
        }
        self.request(url, "post", self.header, data)

if __name__ == '__main__':
     Client().action()