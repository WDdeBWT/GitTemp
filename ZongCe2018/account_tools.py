# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/07"

import time

import openpyxl

import database_model

def verify_account(user_name = '', password = ''):
    al_tb = database_model.tb_AccountList()
    al_tb.open_conn()
    al_list = al_tb.select_data()
    al_tb.close()
    for al in al_list:
        if (user_name == al[0].strip()) and (password == al[1].strip()):
            return al[3].strip()
    return False

def get_class_code(user_name = ''):
    al_tb = database_model.tb_AccountList()
    al_tb.open_conn()
    al_list = al_tb.select_data()
    al_tb.close()
    for al in al_list:
        if user_name == al[0].strip():
            return al[4].strip()
    return False

def update_password(user_name, old_password, new_password):
    flag = False
    al_tb = database_model.tb_AccountList(user_name, new_password)
    al_tb.open_conn()
    al_list = al_tb.select_data()
    for al in al_list:
        if (user_name == al[0].strip()) and (old_password == al[1].strip()):
            flag = True
    if flag == True:
        if al_tb.update_data():
            al_tb.close()
            return True
    al_tb.close()
    return False

def create_account(user_name, password, user_role, real_name = '', class_code = ''):
    flag = False
    al_tb = database_model.tb_AccountList(user_name, password, user_role, real_name, class_code)
    al_tb.open_conn()
    al_list = al_tb.select_data()
    for al in al_list:
        if user_name == al[0].strip():
            flag = True
    if flag == True:
        al_tb.close()
        return 'Error: Stuent user_name existed create_account'
    else:
        if al_tb.insert_data():
            al_tb.close()
            return 'True'
        al_tb.close()
        return 'Error: AccountManagementHandler POST create_question'

def delete_account(user_name):
    flag = False
    al_tb = database_model.tb_AccountList(user_name = user_name)
    al_tb.open_conn()
    al_list = al_tb.select_data()
    for al in al_list:
        if user_name == al[0].strip():
            flag = True
    if flag == False:
        al_tb.close()
        return 'Error: Stuent user_name not exist delete_account'
    else:
        if al_tb.delete_data():
            al_tb.close()
            return 'True'
        al_tb.close()
        return 'Error: AccountManagementHandler POST delete_account'

def init_password(user_name):
    flag = False
    al_tb = database_model.tb_AccountList(user_name, '888888')
    al_tb.open_conn()
    al_list = al_tb.select_data()
    for al in al_list:
        if user_name == al[0].strip():
            flag = True
    if flag == False:
        al_tb.close()
        return 'Error: Stuent user_name not exist init_password'
    else:
        if al_tb.update_data():
            al_tb.close()
            return 'True'
        al_tb.close()
        return 'Error: AccountManagementHandler POST init_password'

def batch_import_users(file_path):
    wb=openpyxl.load_workbook(file_path)
    sheet=wb[(wb.sheetnames[0])]
    rows=[]
    for row in sheet.rows:
        temp=[]
        for item in row:
            temp.append(item.value)
        rows.append(temp)
    rows=rows[2:]
    accountList = database_model.tb_AccountList()
    accountList.open_conn()
    for item in rows:
        accountList.user_name = item[0]
        accountList.password = '666666'
        accountList.user_role = item[1]
        accountList.real_name = item[2]
        accountList.class_code = item[3]
        accountList.insert_data()
        time.sleep(0.05)
    accountList.close()


def show_account():
    show_list = []
    al_tb = database_model.tb_AccountList()
    al_tb.open_conn()
    al_list = al_tb.select_data()
    al_tb.close()
    al_list.sort(key=lambda k: (k[0]))
    for al in al_list:
        if al[0] in ['1101', '1102']:
            continue
        show_list.append([al[2], al[3]])
    return show_list

if __name__=='__main__':
    batch_import_users(r'C:\Users\baiwt\Desktop\评委小组账户.xlsx')