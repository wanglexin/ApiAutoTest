"""
Created on 2020年12月07日
@author: wanglexin
"""

import pymysql


def Api_Data():
    """ 连接数据库配置,上传代码时记得删除或替换配置"""

    connect = pymysql.connect(
        host='',
        port=3306,
        user='',
        password='',
        db='autotest',
        charset='utf8'
    )
    cursor = connect.cursor()
    cursor.execute("select * from api")
    #cursor.execute("select * from api union all select * from api1")
    case = cursor.fetchall()
    cursor.close()
    connect.close()
    return case

if __name__ == '__main__':
    a = Api_Data()