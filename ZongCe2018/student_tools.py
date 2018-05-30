# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/09"

import time
import datetime

import openpyxl

import database_model

def batch_import_student(file_path):
    wb=openpyxl.load_workbook(file_path)
    sheet=wb[(wb.sheetnames[0])]
    rows=[]
    for row in sheet.rows:
        temp=[]
        for item in row:
            temp.append(item.value)
        rows.append(temp)
    rows=rows[2:]
    student_list = database_model.tb_StudentList()
    student_list.open_conn()
    for item in rows:
        student_list.student_id = item[0]
        student_list.student_name = item[1]
        student_list.class_code = item[2]
        student_list.insert_data()
        time.sleep(0.05)
    student_list.close()

def get_student_list(user_name):
    acl = []
    stl = []
    scl = []
    return_list = []
    class_code = ''
    account_list = database_model.tb_AccountList()
    account_list.open_conn()
    acl = account_list.select_data()
    account_list.close()
    for item in acl:
        if item[0] == user_name:
            class_code = item[4]
            break

    student_list = database_model.tb_StudentList()
    student_list.open_conn()
    student_list.class_code = class_code
    stl = student_list.select_data_by_classcode()
    student_list.close()
    
    score_list = database_model.tb_ScoreList()
    score_list.open_conn()
    score_list.eva_id = user_name
    scl = score_list.select_data_by_evaid()
    score_list.close()

    temp_list = [] # students had been evaluated
    for sc in scl:
        temp_list.append(sc[0])

    stl.sort(key=lambda k: (k[0]))
    for st in stl:
        if st[0] in temp_list:
            return_list.append((st[0], "True"))
        else:
            return_list.append((st[0], "False"))
    
    return return_list


def set_score(student_id, eva_id, s1, s2, s3, s4, s5, s6):
    eva_time = datetime.datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
    try:
        score_list = database_model.tb_ScoreList(student_id, eva_id, s1, s2, s3, s4, s5, s6, eva_time)
        score_list.open_conn()
        score_list.insert_data()
        score_list.close()
        return "True"
    except:
        return "ERROR"

def export_score_by_class():
    pass

if __name__ == '__main__':
    li = get_student_list('0121503490301')
    print(li)