# -*- coding:utf-8 -*-
import re
from xlwt import *

file = Workbook(encoding = 'utf-8')
#指定file以utf-8的格式打开
table = file.add_sheet('person_base_message')
#指定打开的文件名

file.save('person_base_message')

table = file.add_sheet('weibo_message')
#指定打开的文件名

file.save('weibo_message')
