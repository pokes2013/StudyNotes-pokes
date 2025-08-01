# 文件名转大写  未完成   番号提取后面多了个点



import os
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter


# 提取文件名


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
    str_fenge_qian = "解决调用循环内临时变量的警告提示"
    numb1 = 0
    while numb1 < wzzb - 1:
        str_fenge_qian = input_file_neme[numb1:wzzb]
        if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
            break
        numb1 += 1

    # 分隔符之后的字符处理
    str_fenge_hou = "解决调用循环内临时变量的警告提示"
    numb2 = wzzb + 2
    while numb2 < 30:
        str_fenge_hou = input_file_neme[wzzb + 1:numb2]
        if is_num(str_fenge_hou):
            pass
        else:
            str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]
            print("纯数字是:" + str_fenge_hou)
            break
        numb2 += 1
        str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]

    # 整合显示结果

    outfile_neme = str_fenge_qian + "-" + str_fenge_hou
    print("番号结果：" + outfile_neme)
    return outfile_neme


# xname = avfile_name_id_draw("jul-032_2K-C.mp4")


# 转换大小写

def dxzh(xstr):
    dname = xstr.upper()
    # print(dname)
    return dname


# dxzh("pokes")

# 改文件名

# os.chdir(r"D:\code\python\99.最终成品\source_data")  # 在对文件重命名之前为其指定路径
#
# for vido in files:
# os.rename(video, result_name)
# print(video)

pathstr = r"D:\code\python\99.最终成品\source_data"

for root, dirs, files in os.walk(pathstr):
    for video in files:
        print(video)
        xname = avfile_name_id_draw(video)
        print(xname)
        dname = dxzh(xname)
        # print(dname)

    # for root, dirs, files in os.walk(filePath):
    #     for video in files:
    #         # 过滤文件格式
    #         wzzb = video.rfind('.')  # 定位最后一个.的位置
    #         hz_name = video[wzzb:]  # 扩展名
    #         print(hz_name)
    #         if hz_name == ".mp4":
    #             # 格式化新文件名
    #             wzzb = video.rfind('.')  # 定位最后一个.的位置
    #             qz_name = video[:wzzb]  # 截取不含扩展名的文件名
    #             hz_name = video[wzzb:]  # 扩展名
    #             result_name = qz_name + houzhui + hz_name
    #
    #             # 重命名
    #             os.chdir(filePath)  # 在对文件重命名之前为其指定路径
    #             os.rename(video, result_name)
    #             print(video)
