# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : 2017/10/20

import os
import win_unicode_console
win_unicode_console.enable()

class pyTest:
    def __init__(self):
        self.read_path = "F:\\Files\\temp\\dir1\\pdf1.pdf"
        self.write_path = "F:\\Files\\temp\\dir2\\pdf2.pdf"
    
    def test1(self):
        bytes_list = []
        with open(self.read_path, 'rb') as r:
            for line in r.readlines():
                bytes_list.append(line)
        return bytes_list
    
    def test2(self, bytes_list):
        with open(self.write_path, 'wb') as w:
            for line in bytes_list:
                w.write(line)

pyt = pyTest()
bytes_list = pyt.test1()
pyt.test2(bytes_list)