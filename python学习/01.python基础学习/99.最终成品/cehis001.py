

import os, sys, time

def vidos(vido_path):

    file_list = os.listdir(vido_path)  # 当前目录所有文件的序列
    vido_hz_list = [".avi", ".flv", ".m4v", ".mkv", ".mp4", ".mov", ".rm", ".rmvb", ".ts", ".vob", ".wmv"]

    full_list = []  # 先新建一个空的列表full_list，用来存放帅选出来的元素
    for vido_hz in vido_hz_list:
        vido_gg_list = [s for s in file_list if vido_hz in s]  # 循环筛选各个后缀的视频列表
        for vido in vido_gg_list:  # 遍历这个列表
            # print(vido)               #打印测试之后出现了重复，例如：abc-999.rm和abc-999.rmvb，因为后缀中都有rm所以同时会被筛选出来
            if vido not in full_list:  # 去重后放入新建的空列表中
                full_list.append(vido)
    print(full_list)

vido_path = os.getcwd()
vidos(vido_path)