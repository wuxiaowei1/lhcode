import pytest
from api.base_request import Client
from tools.read_file import ReadFile

base_url = str(ReadFile.read_config('$.server')["test"])
class Testcode():

    def test_api(self):
        params = {
            "tid": 1,
            "term_id": 107545,
            "camp_day": 1,
            "follow_status": 0
        }
        url = base_url + "/smart/msgs/labels"
        response = Client.baes_request(url, "get", params)
        assert response["code"] == 0

if __name__ == '__main__':
    pytest.main(['-vs']);
