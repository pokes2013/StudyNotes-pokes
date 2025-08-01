import os
from collections import Counter
from pathlib import Path


# 遍历当前文件夹下的文件名

def vidofile(path):
    file_list = os.listdir(path)  # 当前目录所有文件的序列
    return file_list


#  处理文件名

def name_jq(fname):
    wzzb = fname.find('-')  # 定位第一个“-”的具体位置

    # 如果没有“-”,则程序退出处理
    # if wzzb < 1:

    # 循环判断“-”左边是否是纯字母，提取出“-”左边的数据
    pokes1 = wzzb - 1
    while pokes1 < 20:
        # print(pokes1)
        pokes1 = pokes1 - 1
        g_qian = fname[pokes1:wzzb]
        # print(g_qian)
        chun1 = g_qian.isalpha()
        if chun1 is False:
            g_qian = fname[pokes1 + 1:wzzb]
            break

    # 循环判断“-”右边是否是纯数字，提取出“-”右边的数据

    pokes2 = wzzb + 2  # 横岗后第1.2.3....个数字
    while pokes2 < 20:
        # print(pokes)
        pokes2 += 1
        g_hou = fname[wzzb + 1:pokes2]
        chun2 = g_hou.isdigit()
        if chun2 is False:
            # print("不是纯数字了"+g_hou)
            g_hou = fname[wzzb + 1:pokes2 - 1]
            break

    zz = g_qian + "-" + g_hou
    # print(zz)
    return zz


# 判断是否包含,并返回次数

def lisbhstr(instr, datapath):
    datadir = Path(datapath)
    all_list = [file.name for file in datadir.rglob("*.*")]

    pokes_list = [s for s in all_list if instr in s]  # 找出所有搜索结果
    # for file in pokes_list:
    #     print(file)

    cishu = len(pokes_list)  # 获取所有元素个数
    if cishu >= 1:
        print(pokes_list)
        print(instr, "文件貌似重复,请二次确认后删除重复")
    return cishu


# namechuli = name_jq("miae-141.mp4")
# print(namechuli)
# chongfu=lisbhstr(namechuli, r"D:\indexs")


data_index = Path(r"\\10.10.30.99\e\系列专辑-三字节")
index_list = [file.name for file in data_index.rglob("*.mp4")]
# print(index_list)
for vidoname in index_list:
    namechuli = name_jq(vidoname)
    chongfu = lisbhstr(namechuli, r"D:\indexs")
