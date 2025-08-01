# 08.01检验是否重复-不报错版本-思路清晰-已经加入过滤，堪称完美.py

# 发现问题中途会中断

import os
from pathlib import Path
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter


def avfile_name_id_draw(input_file_neme):
    """
    这是一个AV电影番号提取的程序
    :param input_file_neme: 输入你的文件的name
    :return: 返回截取后的new_name
    """

    if "-" in input_file_neme:  # 判断是否包含分隔符

        # 过滤字符
        #     input_file_neme = input_file_neme.replace(',', '').replace('，', '').replace(' ', '').replace('VIP-', '')
        wzzb = input_file_neme.find('-')
        # print(wzzb)

        # 分隔符之前的字符处理
        str_fenge_qian = "解决调用局部或临时遍历警告问题"
        numb1 = 0
        while numb1 < wzzb - 1:
            str_fenge_qian = input_file_neme[numb1:wzzb]
            if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
                break
            numb1 += 1

        # 分隔符之后的字符处理
        str_fenge_hou = "解决调用局部或临时遍历警告问题"
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


def write_txt(strs, txt_name="logs"):
    """
        将文本写入txt
    """
    file = open(txt_name, 'a', encoding='UTF-8')
    file.write(strs)
    file.close()


def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """

    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


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

    if cishu > 0:
        print(pokes_list)
        print(instr, "文件已经存在")
        txt_file = open("logs.txt", 'w', encoding='UTF-8')
        txt_file.write(instr + "文件已经存在\n")
        txt_file.close()
    if cishu > 1:
        print(instr, "文件重复")
        txt_file = open("logs.txt", 'a', encoding='UTF-8')
        txt_file.write(instr + "文件重复重复重复重复重复重复重复重复重复重复\n")
        txt_file.close()
    return cishu


def guolvhaha(lists):
    """
    过滤掉一个列表中的非法字符
    """
    # lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye三级.123456"]
    ffstr_list = ["欧美", "国产", "韩国", "香港", "三级", "$"]  # 将这些视为非法字符
    nowlist=[]
    for vido in lists:
        # print(vido)
        for ffstr in ffstr_list:  # 遍历出需要过滤的字符
            if ffstr in vido or "-" not in vido:  # 如果出现非法字符，则tiaoguo
                # print(vido,"buguize")
                continue
            else:
                # print(vido)
                if vido not in nowlist:
                    nowlist.append(vido)
                    return nowlist



vido_list = file_list(os.getcwd(), "mp4")  # 需要检查的目录
# vido_list = file_list(r"F:\AV2021\001.人妻出轨-家庭教师系列\JUQ系列", "mp4")
vido_list = guolvhaha(vido_list)

for vido in vido_list:
    vido = avfile_name_id_draw(vido)  # 当前目录截取后的vido-name
    result = lisbhstr(vido, r"D:\indexes")


input('Press Enter to exit...')