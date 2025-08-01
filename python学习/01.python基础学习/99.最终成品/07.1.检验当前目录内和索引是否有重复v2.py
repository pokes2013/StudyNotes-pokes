# 此方法用于每个文件夹查找视频文件在索引中是否重复
# 作者：pokes@163.com
# 版本：v1.1

# 还有问题需要修复

# 存在得问题：
    # 1.仅限于类似abc-123这种文件名的格式；
    # 2.大小写的问题，abc-123和ABC-123这两个会识别为不同得文件，无法找出重复
    # 3.不支持不规则得文件名检索，所以检索之前请讲不规则得文件分开



import os
from pathlib import Path
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter

# 提取当前目录内的番号

def ffzf_id(input_file_neme):

    ffstr_list = ["欧美", "国产", "韩国", "香港", "三级", "$"]  # 将这些视为非法字符
    for ffstr in ffstr_list:  # 遍历出需要过滤的字符
        if ffstr in input_file_neme:sys.exit()   # 如果出现非法字符，则程序退出


    # 如果没有“-”,则退出处理
    if "-" not in input_file_neme: sys.exit()  # 判断是否包含分隔符
    return input_file_neme

# 提取当前目录内的番号

def avfile_name_id_draw(input_file_neme):
    """
    这是一个AV电影番号提取的程序
    :param input_file_neme: 输入你的文件的name
    :return: 返回截取后的new_name
    """

    # 过滤非法字符
    ffstr_list = ["欧美", "国产", "韩国", "香港", "三级", "$"]  # 将这些视为非法字符
    for ffstr in ffstr_list:  # 遍历出需要过滤的字符
        if ffstr in input_file_neme: sys.exit()  # 如果出现非法字符，则程序退出

    # 如果没有“-”,则退出处理
    if "-" not in input_file_neme: sys.exit()  # 判断是否包含分隔符

    # 过滤字符
    input_file_neme = input_file_neme.replace(',', '').replace('，', '').replace(' ', '').replace('VIP-', '')
    wzzb = input_file_neme.find('-')
    # print(wzzb)

    # 分隔符之前的字符处理
    numb1 = 0
    while numb1 < wzzb - 1:
        str_fenge_qian = input_file_neme[numb1:wzzb]
        if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
            break
        numb1 += 1

    # 分隔符之后的字符处理

    numb2 = wzzb + 2
    while numb2 < 30:
        str_fenge_hou = input_file_neme[wzzb + 1:numb2]
        if is_num(str_fenge_hou):
            pass
        else:
            str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]
            # print("纯数字是:" + str_fenge_hou)
            break
        numb2 += 1
        str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]

        # 整合显示结果

        outfile_neme = str_fenge_qian + "-" + str_fenge_hou
    return outfile_neme


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


# 检查重复

vido_list = file_list(r"F:\AV2021\001.人妻出轨-家庭教师系列\JUQ系列", "mp4")  # 需要检查的目录
pathsss = r"D:\indexes"  # 索引目录
for vido in vido_list:
    guolv1 = ffzf_id(vido)   # 番号非法字符
    # print(guolv1)
    guolv2 = avfile_name_id_draw(guolv1)  # 番号过滤
    # print(guolv2)
    # # print(fnahao)
    pdcf=lisbhstr(guolv2, pathsss)
