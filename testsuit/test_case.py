from common.api_handle import Api_Handle
from data.api_db import Api_Data
from logs.get_logger import get_log
from common.send_msg import send_MSG
import pytest
import time

class TestClass(object):

    def test_forApi(self):
        api_data = Api_Data()
        sms = send_MSG()
        logger = get_log("api.log")

        for i in range(len(api_data)):
            api_handle = Api_Handle(api_data[i])
            res = api_handle.send_request()
            # try:
            #     assert api_handle.get_code() in res.text
            #     assert api_handle.get_msg() in res.text
            #     logger.info(api_handle.get_api_name()+"接口执行成功")
            #
            # except Exception as e:
            #     #sms.send_msg_txt(api_handle.get_api_name(), str(e))
            #     logger.error(str(api_handle.get_api_id())+api_handle.get_api_name()+"接口执行失败")

            if api_handle.get_code() and api_handle.get_msg() not in res.text:
                '''
                    方法介绍：
                        这个判断是为了判断接口测试用例中的code是否包含在接口返回值中
                        如果不包含那么则重新调用一次接口
                        因为扫码中可能按摩椅状态不是空闲中，所以需要等待一段时间后重新执行
                        避免因为按摩椅状态误报
                '''
                time.sleep(3)
                api_handle.send_request()
                try:
                    assert api_handle.get_code() in res.text
                    assert api_handle.get_msg() in res.text
                    logger.info(api_handle.get_api_name()+"接口执行成功")

                except Exception as e:
                    sms.send_msg_txt(api_handle.get_api_name(), str(e))
                    logger.error(api_handle.get_api_name()+"接口执行失败")
            else:
                logger.info(api_handle.get_api_name()+"接口执行成功")

if __name__ == '__main__':
    pytest.main(['test_case.py'])