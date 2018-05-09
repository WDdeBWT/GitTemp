# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/09"

import time

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