# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/07"

import csv
import time

import pymssql


class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    """

    def __init__(self):
        """
        建立连接
        得到连接信息
        返回: conn.cursor()
        """

        # 配置信息
        # imf_path = r'C:\Baiwt\Files\mssql_account.csv' # XPS13
        # db_host = '119.23.239.27'
        imf_path = r'C:\Files\mssql_account.csv' # Aliyun_Bai
        db_host = '127.0.0.1'
        db_user = 'WeiboSpiderUser'
        db_password = ''
        db_database = 'ZongCe2018'
        db_charset = "utf8"

        # 打开 mssql_account.csv
        act_list = []
        with open(imf_path) as f:
            reader = csv.reader(f)
            act_list = list(reader)
        for act in act_list:
            if act[0].strip() == db_user.strip():
                db_password = act[1].strip()
                break

        self.conn = pymssql.connect(host=db_host, user=db_user, password=db_password, database=db_database, charset=db_charset)
        # self.conn=pymssql.connect(host='.',database='WeiboSpiderDB', charset="utf8")
        self.cur = self.conn.cursor()
        if self.cur:
            pass
            # print("连接数据库成功")
        else:
            print("连接数据库失败")

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        """
        self.cur.execute(sql)
        resList = self.cur.fetchall()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        """
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            print("^TIME^: " + str(time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))))
            return False
    
    def close_connection(self):
        self.conn.close()

# conn = pymssql.connect(host = '119.23.239.27', database = 'GuestBook', user = 'WeiboSpiderUser', password = 'weibospideruser')
# cur = conn.cursor()
# cur.excute("SELECT * FROM tbGuestBook")