# 提取当前目录内的番号

import os
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter


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
    str_fenge_qian = "解决调用局部或临时遍历井盖问题"
    numb1 = 0
    while numb1 < wzzb - 1:
        str_fenge_qian = input_file_neme[numb1:wzzb]
        if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
            break
        numb1 += 1

    # 分隔符之后的字符处理
    str_fenge_hou = "解决调用局部或临时遍历井盖问题"
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


f=avfile_name_id_draw("12312321abcd-123411-dwjidwjwid.mp4")
print(f)