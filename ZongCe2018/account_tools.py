# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/07"

import os
import time
import shutil

import openpyxl
import numpy as np
from PIL import Image

import ZongCe
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

def batch_import_user(file_path):
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

def batch_import_user_online(data_bytes):
    file_path = os.path.join(ZongCe.settings['file_path'] + '\\temp\\', 'temp.xlsx')
    with open(file_path, 'wb') as up:
        up.write(data_bytes)
    batch_import_user(file_path)
    

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
    batch_import_user(r'C:\Users\baiwt\Desktop\评委小组账户.xlsx')

def get_picture(user_name):
    avatar_id = None
    ad_tb = database_model.tb_AccountDetail(user_name)
    ad_tb.open_conn()
    avatar_list = ad_tb.select_data_by_username()
    if avatar_list:
        avatar_id = avatar_list[0][2]
    ad_tb.close()
    if avatar_id:
        shutil.copyfile(os.path.join(ZongCe.settings['file_path'] + '\\profile_picture\\', str(avatar_id).strip() + '.jpg')
            , os.path.join(ZongCe.settings['static_path'] + '\\profile_picture\\', str(avatar_id).strip() + '.jpg'))
        return 'http://' + ZongCe.settings['server_ip'] + '/static/profile_picture/' + str(avatar_id) + '.jpg'
    else:
        return 'http://' + ZongCe.settings['server_ip'] + '/static/profile_picture/default.jpg'

def upload_picture(user_name, file_name, file_bytes):
    temp_path = os.path.join(ZongCe.settings['file_path'] + '\\temp\\', file_name)
    with open(temp_path, 'wb') as up:
        up.write(file_bytes)
    ad_tb = database_model.tb_AccountDetail(user_name)
    ad_tb.open_conn()
    # 获取新图片编号并存入数据库
    new_avatar_id = ad_tb.update_avatar()
    ad_tb.close()
    if not new_avatar_id:
        return 'False'
    save_path = os.path.join(ZongCe.settings['file_path'] + '\\profile_picture\\', str(new_avatar_id).strip() + '.jpg')
    # PIL库联合numpy库处理图片
    ori_img = Image.open(temp_path)
    template_size = min(ori_img.width, ori_img.height) // 2
    center_width = ori_img.width // 2
    center_height = ori_img.height // 2
    region = ((center_width-template_size), (center_height-template_size), (center_width+template_size), (center_height+template_size))
    new_img = ori_img.crop(region)
    new_img.save(save_path)
    # 复制文件到static目录
    return 'True'