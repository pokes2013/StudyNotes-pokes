# 此方法用于每个文件夹查找视频文件在索引中是否重复
# 作者：pokes@163.com
# 版本：v1.0


# 存在得问题：
# 1.仅限于类似abc-123这种文件名的格式；
# 2.大小写的问题，abc-123和ABC-123这两个会识别为不同得文件，无法找出重复
# 3.不支持不规则得文件名检索，所以检索之前请讲不规则得文件分开


import os
from pathlib import Path


# 提取当前目录内的番号

def fanhao_id(file_name):
    wzzb = file_name.find('-')  # 获取分隔符的位置

    # 分隔符之前的字符处理
    numb1 = 0
    while numb1 < wzzb - 1:
        file_name_qz = file_name[numb1:wzzb]
        if (file_name_qz.isalpha()):  # 检测是不是纯字母isalpha()
            # print("纯字母是:" + file_name_qz)
            break
        numb1 += 1

    # 分隔符之后的字符处理

    numb2 = wzzb + 2
    # print(numb2)
    while numb2 < 10:
        file_name_hz = file_name[wzzb + 1:numb2]
        if not (file_name_hz.isdigit()):
            file_name_hz = file_name[wzzb + 1:numb2 - 1]
            # print("纯数字是",file_name_hz)
            break
        numb2 += 1

    fanhao = file_name_qz + "-" + file_name_hz
    # print(fanhao)
    return fanhao


# 判断是否包含,并返回次数

def lisbhstr(instr, datapath):
    """
    判断输入的字符串instr，是否包含在索引datapath目录
    :param instr:的字符串instr
    :param datapath:索引datapath目录
    :return:返回instr字符串在，datapath目录所有文件名中出现的次数
    """

    # 这个是from pathlib import Path模块的方法
    datadir = Path(datapath)
    all_list = [file.name for file in datadir.rglob("*.*")]

    pokes_list = [s for s in all_list if instr in s]  # 找出所有搜索结果
    cishu = len(pokes_list)  # 获取所有元素个数
    if 2 > cishu > 0:
        # print(pokes_list)
        # print(instr, "文件已经存在")
        file = open("logs.txt", 'a', encoding='UTF-8')
        file.write(instr + "文件已经存在\n")
    if cishu > 2:
        print(pokes_list)
        print(instr, "文件重复")
        file.write(instr + "文件重复重复重复重复重复重复重复重复重复重复\n")
        file.close()

    return cishu


def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


# 测试

# strsssss="STAR-259-C-羽田爱.mp4"
# pathssss=r"D:\indexs"
# strsssss=fanhao_id(strsssss)
# haha=lisbhstr(strsssss,pathssss)
# print(haha)

# 检查重复

vido_list = file_list(r"F:\AV2021\001.人妻出轨-家庭教师系列\JUQ系列", "mp4")  # 需要检查的目录
pathsss = r"D:\indexs"  # 索引目录
for vido in vido_list:
    fnahao = fanhao_id(vido)  # 番号过滤
    # print(fnahao)
    lisbhstr(fnahao, pathsss)

os.system(“pause”)
