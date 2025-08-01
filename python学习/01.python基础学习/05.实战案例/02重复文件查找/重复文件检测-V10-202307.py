
# 还没有完成

import re, os

# 遍历文件及子文件

#遍历dir路径下,所有文件.含子目录，最终结果只显示文件名

def file_name_list(dir):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(filename)
    # 排除关键字
    list1 = ['片头', '国产', '欧美', '3D', 'milky',
             '三级', '香港', '韩国', '麻豆', '夜桜', '动漫', '蒂法', '换脸']  # 排除关键字列表

    filter_data_paichu = [x for x in files_list if all(y not in x for y in list1)]

    # 过滤出视频文件

    vido_list = [".avi", ".f4v", ".flv", ".m4p", ".m4v", ".mkv", ".mp4", ".mp4v",
                 ".mpe", ".mpeg", ".mpg", ".mpv4", ".mov", ".rm",
                 ".rmvb", ".swf", ".ts", ".vob", ".vp6", ".wm", ".wmv"
                                                                ".AVI", ".F4V", ".FLV", ".M4P", ".M4V", ".MKV", ".MP4",
                 ".MP4V",
                 ".MPE", ".MPEG", ".MPG", ".MPV4", ".MOV", ".RM",
                 ".RMVB", ".SWF", ".TS", ".VOB", ".VP6", ".WM", ".WMV"
                 ]  # 需要的包含的字符串

    result_list = []  # 新建空列表用于存放生成的新数据

    for i in vido_list:
        linshi_list = [s for s in filter_data_paichu if i in s]
        for a in linshi_list:
            if a not in result_list:
                result_list.append(a)
    # print(result_list)

    # print(files_list)        #所有文件的绝对路径
    return result_list

#遍历某个路径下的abc-123这种格式的文件名，并生成一个序列
def avipath_nameid(inpath):
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        if "mp4" or "mkv" or "avi" in vido_name:
            result = re.findall(r'[a-zA-Z]{2,6}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # print(fanhao)
                if fanhao not in list:
                    # print(fanhao)
                    list.append(fanhao.upper())
    # print(list)
    return list



# 先遍历出索引数据库,规范格式为MEYD-451

data_list = avipath_nameid(r"D:\indexes")
# # print(data_list)


# # 遍历出需要对比的文件名，规范格式为MEYD-451
# # vido_list = avipath_nameid(r"F:\AV2021")
vido_list = avipath_nameid(os.getcwd())


#循环对比出当前目录类重复的文件

for vido_name in vido_list:
    linshi_list = [s for s in data_list if vido_name in s]
    cishu = len(linshi_list)

    if cishu > 0:
        print(vido_name, "文件重复")
        file = open("chongfu_logs.txt", 'a', encoding='UTF-8')
        file.write(vido_name + "警告：文件重复，文件重复，文件重复\n")
        file.close()


# input('Press Enter to exit...')