import requests

class send_MSG :
    # 文本类型消息
    def send_msg_txt(self, request_name, msg):
        headers = {"Content-Type": "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*************************"  #群机器人的Webhook
        send_data = {
            "msgtype": "text",  # 消息类型，此时固定为text
            "text": {
                "content": "接口自动化执行完成，线上接口运行时报错，接口名称为:"+request_name+"，报错信息为"+msg,  # 文本内容，最长不超过2048个字节，必须是utf8编码
                "mentioned_list": ["@all"]
            }
        }

        requests.post(url=send_url, headers=headers, json=send_data)

if __name__ == '__main__' :
    sms = send_MSG()

    name = sms.send_msg_txt('测试环境扫码','404')