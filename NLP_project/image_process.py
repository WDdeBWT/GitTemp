# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/01/08"

import os
import sys
import time

import numpy as np
from PIL import Image

class ImageProcess:
    def __init__(self, read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path
    
    def cut_img(self, img, img_name):
        img_array = np.array(img)
        save_path = os.path.join(self.write_path, img_name)
        save_path = save_path[:-4] # 去除文件名尾部的.jpg
        special_img = []
        if (img.width > 3800) or (img.height > 15200):
            print("---sepcial_img: " + img_name)
            special_img.append(img_name)
        
        # 图片高度小于3900的情况，不剪裁直接保存
        elif img.height < 3900:
            print("正在处理：" + img_name + "，高度：" + str(img.height) + "，裁成1张")
            img.save(save_path + "_part1.jpg")
        
        # 图片高度在3900值7700之间的情况，裁成两张
        elif (img.height >= 3900) and (img.height < 7700):
            print("正在处理：" + img_name + "，高度：" + str(img.height) + "，裁成2张")
            for i in range(100):
                flag = 0
                for im in img_array[i+3800]:
                    if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                        flag += 1
                if (flag > 10) and (i != 99):
                    continue
                else:
                    region_1 = (0, 0, img.width, i+3800)
                    region_2 = (0, i+3800, img.width, img.height)
                    new_img_1 = img.crop(region_1)
                    new_img_2 = img.crop(region_2)
                    new_img_1.save(save_path + "_part1.jpg")
                    if new_img_2.height > 80:# 高度小于80的图片被认为是边角料，没有有效信息
                        new_img_2.save(save_path + "_part2.jpg")
                    break
        
        # 图片高度在7700值11500之间的情况，裁成三张
        elif (img.height >= 7700) and (img.height < 11500):
            print("正在处理：" + img_name + "，高度：" + str(img.height) + "，裁成3张")
            cut_1 = 0
            cut_2 = 0
            for i in range(100):
                flag_1 = 0
                flag_2 = 0
                # 寻找第一个切割点，3800附近
                if cut_1 == 0:
                    for im in img_array[i+3800]:
                        if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                            flag_1 += 1
                    if flag_1 < 10:
                        cut_1 = i+3800
                # 寻找第二个切割点，7600附近
                if cut_2 == 0:
                    for im in img_array[i+7600]:
                        if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                            flag_2 += 1
                    if flag_2 < 10:
                        cut_2 = i+7600
            if cut_1 == 0:
                cut_1 = 3800
            if cut_2 == 0:
                cut_2 = 7600
            region_1 = (0, 0, img.width, cut_1)
            region_2 = (0, cut_1, img.width, cut_2)
            region_3 = (0, cut_2, img.width, img.height)
            new_img_1 = img.crop(region_1)
            new_img_2 = img.crop(region_2)
            new_img_3 = img.crop(region_3)
            new_img_1.save(save_path + "_part1.jpg")
            new_img_2.save(save_path + "_part2.jpg")
            if new_img_3.height > 80:# 高度小于80的图片被认为是边角料，没有有效信息
                new_img_3.save(save_path + "_part3.jpg")
            
        # 图片高度在11500值15300之间的情况，裁成四张
        elif (img.height >= 11500) and (img.height < 15300):
            print("正在处理：" + img_name + "，高度：" + str(img.height) + "，裁成4张")
            cut_1 = 0
            cut_2 = 0
            cut_3 = 0
            for i in range(100):
                flag_1 = 0
                flag_2 = 0
                flag_3 = 0
                # 寻找第一个切割点，3800附近
                if cut_1 == 0:
                    for im in img_array[i+3800]:
                        if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                            flag_1 += 1
                    if flag_1 < 10:
                        cut_1 = i+3800
                # 寻找第二个切割点，7600附近
                if cut_2 == 0:
                    for im in img_array[i+7600]:
                        if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                            flag_2 += 1
                    if flag_2 < 10:
                        cut_2 = i+7600
                # 寻找第三个切割点，11400附近
                if cut_3 == 0:
                    for im in img_array[i+11400]:
                        if (im < 220).any():# 若any小于220的超过10个点，则认为压到字了
                            flag_3 += 1
                    if flag_3 < 10:
                        cut_3 = i+11400
            if cut_1 == 0:
                cut_1 = 3800
            if cut_2 == 0:
                cut_2 = 7600
            if cut_3 == 0:
                cut_3 = 11400
            region_1 = (0, 0, img.width, cut_1)
            region_2 = (0, cut_1, img.width, cut_2)
            region_3 = (0, cut_2, img.width, cut_3)
            region_4 = (0, cut_3, img.width, img.height)
            new_img_1 = img.crop(region_1)
            new_img_2 = img.crop(region_2)
            new_img_3 = img.crop(region_3)
            new_img_4 = img.crop(region_4)
            new_img_1.save(save_path + "_part1.jpg")
            new_img_2.save(save_path + "_part2.jpg")
            new_img_3.save(save_path + "_part3.jpg")
            if new_img_4.height > 80:# 高度小于80的图片被认为是边角料，没有有效信息
                new_img_4.save(save_path + "_part4.jpg")
                
    def main(self):
        file_list = os.listdir(self.read_path)
        for file_name in file_list:
            file_path = os.path.join(self.read_path, file_name)
            img = Image.open(file_path)
            self.cut_img(img, file_name)

path_read = 'F:\\Files\\weibo_taobaibai\\image'
path_write = 'F:\\Files\\weibo_taobaibai\\new'
img_prc = ImageProcess(path_read, path_write)
img_prc.main()
print("-----finish-----")
