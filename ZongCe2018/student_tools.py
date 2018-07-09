# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/09"

import time
import datetime

import openpyxl

import database_model
import account_tools

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
    stl = []
    scl = []
    result_list = []
    class_code = account_tools.get_class_code(user_name)
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
            result_list.append([st[0], st[1], "True"])
        else:
            result_list.append([st[0], st[1], "False"])
    
    return result_list


def set_score(student_id, eva_id, score_list):
    s1 = score_list[0]
    s2 = score_list[1]
    s3 = score_list[2]
    s4 = score_list[3]
    s5 = score_list[4]
    s6 = score_list[5]
    eva_time = datetime.datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
    try:
        score_list = database_model.tb_ScoreList(student_id, eva_id, s1, s2, s3, s4, s5, s6, eva_time)
        score_list.open_conn()
        score_list.insert_data()
        score_list.close()
        return "True"
    except:
        return "ERROR"

def export_score_by_class(class_code):
    stl = []
    scl = []
    fmt_list = []
    result_list = []

    student_list = database_model.tb_StudentList()
    student_list.open_conn()
    student_list.class_code = class_code
    stl = student_list.select_data_by_classcode()
    student_list.close()

    score_list = database_model.tb_ScoreList()
    score_list.open_conn()
    scl = score_list.select_data()
    score_list.close()

    stl.sort(key=lambda k: (k[0]))
    for st in stl:
        temp_list = [st[0], st[1]]
        for sc in scl:
            if sc[0] == st[0]:
                temp_list.append(sc)
        fmt_list.append(temp_list) # fmt_list: [[st[0], st[1], (sc[0], sc[1], ...), (...), ...], [...], ...]

    for item in fmt_list:
        temp_list = []
        score_sum = 0
        if len(item) < 7:
            # If the number of judges are less than five
            result_list.append([item[0], item[1], "-1", '---'])
        else:
            for sub_item in item[2:]:
                temp_sum = 0
                temp_sum = sub_item[2] + sub_item[3] + sub_item[4] + sub_item[5] + sub_item[6] + sub_item[7]
                temp_list.append(temp_sum)
            temp_list.sort()
            for tl in temp_list[1:-1]:
                score_sum += tl
            result_list.append([item[0], item[1], str(round((score_sum / (len(temp_list) - 2)), 2)), str(len(temp_list))])

    return result_list


if __name__ == '__main__':
    batch_import_student(r'C:\Users\baiwt\Desktop\班级学生列表.xlsx')