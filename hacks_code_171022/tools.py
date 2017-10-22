# -*- coding:utf-8 -*-
from xlwt import *
from xlrd import open_workbook
from xlutils.copy import copy

class Tools:

    @staticmethod
    def write_aperson(person):
        rexcel = open_workbook("person_base_message")  # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows
        excel = copy(rexcel)
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet

        # add a row
        row = rows
        table.write(row, 0, "id")
        table.write(row, 1, person.name.decode('utf-8'))
        table.write(row, 2, person.num_weibo)
        table.write(row, 3, person.num_watch)
        table.write(row, 4, person.num_fans)

        excel.save("person_base_message")

    @staticmethod
    def write_aweibo(weibo):
        rexcel = open_workbook("weibo_message")  # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows
        excel = copy(rexcel)
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet

        # add a row
        row = rows
        table.write(row, 0, weibo.id)
        table.write(row, 1, weibo.time)
        table.write(row, 2, weibo.num_like)
        table.write(row, 3, weibo.num_resend)
        table.write(row, 4, weibo.num_comment)
        table.write(row, 5, weibo.content)

        excel.save("weibo_message")
