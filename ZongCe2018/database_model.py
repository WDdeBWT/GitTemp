# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/07"

import time

from ms_sql import MSSQL

def freeExecute(sql_str, is_select):
    ms_sql = MSSQL()
    if is_select:
        return_content =  ms_sql.ExecQuery(sql_str)
    else:
        if ms_sql.ExecNonQuery(sql_str):
            return_content = True
        else:
            print("---------- freeExecute 自由执行语句失败 ----------")
            return_content = False
    ms_sql.close_connection()
    return return_content


class tb_AccountList:
    def __init__(self, user_name = '', password = '', user_role = '',real_name=''):
        self.user_name = user_name
        self.password = password
        self.user_role = user_role
        self.real_name = real_name
        self.ms_sql = None
    
    def open_conn(self):
        self.ms_sql = MSSQL()

    def close(self):
        self.ms_sql.close_connection()
    
    def insert_data(self):
        sql = "INSERT INTO accountList VALUES('" + str(self.user_name) + "', '" + str(self.password) + "', '" + str(self.user_role) +"','"+ str(self.real_name) + "')"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_AccountList 保存到数据库失败 ----------")
            return False

    def delete_data(self):
        sql = "DELETE FROM accountList WHERE user_name = '" + self.user_name + "'"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_AccountList 删除到数据库失败 ----------")
            return False 

    def select_data(self):
        sql = "SELECT * FROM accountList"
        return self.ms_sql.ExecQuery(sql)
    
    def update_data(self):
        sql = "UPDATE accountList SET password = '" + self.password + "' WHERE user_name = '" + self.user_name + "'"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_AccountList 更新到数据库失败 ----------")
            return False