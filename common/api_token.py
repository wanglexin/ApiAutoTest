# -*- coding=utf-8 -*-，
import configparser
import os
import requests


"""
    方法介绍：
        获得token，并根据项目名称来判断不同的环境使用的不同的token
"""

def get_token(terrace):

    if terrace == '测试环境扫码':
        pass
        # r = redis.Redis(host='', port=, password='', db=0)
        # if r.hexists(name="UX_TOKEN:wlxuxtoken1", key="TERRACE_ID"):
        #     pass
        # else:
        #     r.hset(name="UX_TOKEN:wlxuxtoken1", key="TERRACE_ID", value="")
        #     r.hset(name="UX_TOKEN:wlxuxtoken1", key="OPENID", value="")
        #
        # if r.hexists(name="UX_TOKEN:wlxuxtoken2", key="TERRACE_ID"):
        #     pass
        # else:
        #     r.hset(name="UX_TOKEN:wlxuxtoken2", key="TERRACE_ID", value="")
        #     r.hset(name="UX_TOKEN:wlxuxtoken2", key="OPENID", value="")
        #
        # if r.hexists(name="UX_TOKEN:wlx_JD_ux_token", key="TERRACE_ID"):
        #     pass
        # else:
        #     r.hset(name="UX_TOKEN:wlx_JD_ux_token", key="TERRACE_ID", value="")
        #     r.hset(name="UX_TOKEN:wlx_JD_ux_token", key="OPENID", value="")

    elif terrace == '测试环境扫码':
        pass

    else:
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录
        cf = configparser.ConfigParser()
        cf.read(root_dir+"/api_config.ini", encoding='utf-8')  # 拼接得到config.ini文件的路径，直接使用
        urls = cf.get(terrace, 'urls')
        data = cf.get(terrace, 'data')
        res = requests.post(url=urls, data=eval(data))
        token = res.json()['items']['token']
        return token


if __name__ == '__main__':
    get_token()