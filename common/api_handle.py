"""
@author: wanglexin
"""

from common import api_token
import requests

class Api_Handle(object):

    def __init__(self, parameter):
        self.id = parameter[0]
        self.request_name = parameter[1]
        self.request_type = parameter[2]
        self.request_url = parameter[3]
        self.request_params = parameter[4]
        self.request_headers = parameter[5]
        self.code = parameter[6]
        self.msg = parameter[7]
        self.is_token = parameter[8]

    def send_request(self):
        if self.request_type not in ['GET', 'POST']:
            print('请先区分大小写！')
            return
        if self.is_token == "1":
            token = api_token.get_token(self.request_name)
            res = requests.request(method=self.request_type, url=self.request_url, params=eval(self.request_params.encode("utf-8").decode("latin1")), headers=eval(self.request_headers % token))
            return res
        else:
            res = requests.request(method=self.request_type, url=self.request_url, params=eval(self.request_params.encode("utf-8").decode("latin1")), headers=eval(self.request_headers.encode("utf-8").decode("latin1")))
            return res

    #提取接口用例中的code,后面用断言来判断
    def get_code(self):
        return self.code

    #提取接口用例中的code
    def get_msg(self):
        return self.msg

    #提取接口用例中的名称
    def get_api_name(self):
        return self.request_name

    #提取接口用例中的名称
    def get_api_id(self):
        return self.id



if __name__ == '__main__':
    a = (601, '07.查询用户选中卡券状态(锁定状态),App下不传token（传入错误及null）', 'GET', 'http://baidu.com', '{\'null\': \'null\'}', '{\'null\': \'null\'}', '0', 'ok', 0)
    b = Api_Handle(a)
    print(b.request_name)
    print(b.request_type)
    print(b.request_url)
    print(b.request_params)
    print(b.request_headers)
    print(b.code)
    print(b.msg)
    x = b.send_request()

