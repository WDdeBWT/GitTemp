# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/01/08"

import os
import sys
import csv
import time

from aip import AipOcr


class ImageOCR:
    def __init__(self):
        APP_ID = '10492378'
        API_KEY = 'PeclifhsWLy991bIxA3OC5ab'
        SECRET_KEY = '0DdKiWzikvFylgvg5kQqLnZwHVCnU2r9'
        self.options = {
            'detect_direction': 'true',
            'language_type': 'CHN_ENG',
        }
        self.file_directory = "D:\\code\\file"
        self.write_path = 'D:\\code\\1.csv'
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()
    
    def write_csv(self, content_list):
        fieldnames = ["FILE_NAME", "CONTENT"]
        with open(self.write_path, 'w', newline="") as w:
            writer = csv.DictWriter(w, fieldnames=fieldnames)
            writer.writerows(content_list)
    
    def main(self):
        content_list = []
        error_list = []
        file_list = os.listdir(self.file_directory)
        for file_name in file_list:
            words = ''
            file_path = os.path.join(self.file_directory, file_name)
            try:
                time.sleep(1)
                result = self.client.basicGeneral(self.get_file_content(file_path), self.options)
                for word in result['words_result']:
                    words = words + ',' + word['words']
                print(words[:20] + "...")
                content_list.append({"FILE_NAME": file_name, "CONTENT": words})
            except Exception as e:
                error_list.append(file_name)
                print(e)
        self.write_csv(content_list)
        print("----------FINISH----------")
        for err in error_list:
            print("error: " + err)

img_ocr = ImageOCR()
img_ocr.main()



