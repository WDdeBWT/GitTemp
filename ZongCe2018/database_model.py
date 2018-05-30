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
    def __init__(self, user_name = '', password = '', user_role = '', real_name = '', class_code = ''):
        self.user_name = user_name
        self.password = password
        self.user_role = user_role
        self.real_name = real_name
        self.class_code = class_code
        self.ms_sql = None
    
    def open_conn(self):
        self.ms_sql = MSSQL()

    def close(self):
        self.ms_sql.close_connection()
    
    def insert_data(self):
        sql = "INSERT INTO accountList VALUES('" + str(self.user_name) + "', '" + str(self.password) + "', '" + str(self.user_role) + "','" + str(self.real_name) + "','" + str(self.class_code) + "')"
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


class tb_StudentList:
    def __init__(self, student_id = '', student_name = '', class_code = ''):
        self.student_id = student_id
        self.student_name = student_name
        self.class_code = class_code
        self.ms_sql = None
    
    def open_conn(self):
        self.ms_sql = MSSQL()

    def close(self):
        self.ms_sql.close_connection()
    
    def insert_data(self):
        sql = "INSERT INTO studentList VALUES('" + str(self.student_id) + "', '" + str(self.student_name) + "','" + str(self.class_code) + "')"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_StudentList 保存到数据库失败 ----------")
            return False

    def delete_data(self):
        sql = "DELETE FROM studentList WHERE student_id = '" + self.student_id + "'"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_StudentList 删除到数据库失败 ----------")
            return False 

    def select_data(self):
        sql = "SELECT * FROM studentList"
        return self.ms_sql.ExecQuery(sql)
    
    def select_data_by_classcode(self):
        sql = "SELECT * FROM studentList WHERE class_code = '" + str(self.class_code) + "'"
        return self.ms_sql.ExecQuery(sql)


class tb_ScoreList:
    def __init__(self, student_id = '', eva_id = '', s1 = '', s2 = '', s3 = '', s4 = '', s5 = '', s6 = '', eva_time = ''):
        self.student_id = student_id
        self.eva_id = eva_id
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.eva_time = eva_time
        self.ms_sql = None
    
    def open_conn(self):
        self.ms_sql = MSSQL()

    def close(self):
        self.ms_sql.close_connection()
    
    def insert_data(self):
        sql = "INSERT INTO scoreList VALUES('" + str(self.student_id) + "', '" + str(self.eva_id) + "', " + str(self.s1) + ", " + str(self.s2) + ", " + str(self.s3) + ", " + str(self.s4) + ", " + str(self.s5) + ", " + str(self.s6) + ", '" + str(self.eva_time) + "')"
        if self.ms_sql.ExecNonQuery(sql):
            return True
        else:
            print("---------- tb_ScoreList 保存到数据库失败 ----------")
            return False

    def select_data(self):
        sql = "SELECT * FROM scoreList"
        return self.ms_sql.ExecQuery(sql)
    
    def select_data_by_evaid(self):
        sql = "SELECT * FROM scoreList WHERE eva_id = '" + str(self.eva_id) + "'"
        return self.ms_sql.ExecQuery(sql)
