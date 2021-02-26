import json
import os
import pymysql



class read_Json():

    def __init__(self):
        json_path = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录
        self.filename = open(os.path.join(json_path, '按摩椅扫码.postman_collection.json'), encoding='utf8')

    def read_json(self):
        """
            字段含义：
                requestJson:读取json文件中的整个json体
                item:读取json体中的跟接口有关的信息（字典格式）
                jsonHeader:jeson文件的header，取出来后需要重新转成字典格式
                           因为格式是"key": "chair_id","value": "1"，这种所以需要转换成"chair_id"："1"这种存到数据库中
                jsonBody:jeson文件的Body，取出来后需要重新转成字典格式（如上）
                method：读取json文件中的get或者post
                header：字面意义上的接口需要的header
                url：字面意义上的接口需要的url
                body：字面意义上的接口需要的body(实际上就是params参数)
            方法介绍：
                该方法是使用postman接口测试后，直接导出成json文件，然后通过这个方法直接插入到数据库中
                避免需要重复工作

        """
        request_json = json.load(self.filename)
        item = request_json['item']
        id = 10
        for i in range(len(item)):
            for x in range(len(item[i]['item'])):
                id = id + 1
                request_name = item[i]['name']+','+item[i]['item'][x]['name']
                method = item[i]['item'][x]['request']['method']
                header = {}
                url = item[i]['item'][x]['request']['url']['raw']
                body = {}
                json_Header = self.is_null(item[i]['item'][x]['request'], 'header')
                json_Body = self.is_null(item[i]['item'][x]['request']['url'], 'query')

                for y in range(len(json_Header)):
                    if "token" in json_Header[y]['key']:
                        header[json_Header[y]['key']] = '%s'
                    else:
                        header[json_Header[y]['key']] = json_Header[y]['value']

                for x in range(len(json_Body)):
                    body[json_Body[x]['key']] = json_Body[x]['value']
                #print(self.split_Sql(id, request_name, method, url, body, header))
                self.exec_sql(self.split_Sql(id, request_name, method, url, body, header))


    def split_Sql(self, id, request_name, method, url, header, body):
        sql = 'INSERT INTO `api` (`id`, `Name`, `Request`, `Url`, `Data`, `Headers`, `Pattern`, `Report`, `is_token`) VALUES ("%s","%s","%s","%s","%s","%s","0","ok","0");' % (id, request_name, method, url, body, header)
        return sql

    def exec_sql(self, sql):
        """ 连接数据库配置,上传代码时记得删除或替换配置"""
        connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            db='autotest',
            charset='utf8'
        )
        cursor = connect.cursor()
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()

    def is_null(self, a, b):
        if 'query' in a.keys():
            return a[b]
        else:
            list1 =[]
            list1.append({'key': 'null', 'value': 'null'})
            return list1

if __name__ == '__main__':
    a = read_Json()
    a.read_json()