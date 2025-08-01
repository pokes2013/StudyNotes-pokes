
import re, os


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
    # print(files_list)        #所有文件的绝对路径
    return files_list


def avipath_nameid(inpath):
    """
        提取番号，转换为大写，写入到list列表中
    """
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        s = vido_name.split(".")
        ss = s[len(s) - 1]
        if (ss == "mp4" or ss == "MP4" or
                ss == "wmv" or ss == "WMV" or
                ss == "avi" or ss == "AVI" or
                ss == "rmvb" or ss == "rmvb" or
                ss == "rm" or ss == "RM" or
                ss == "mov" or ss == "MOV" or
                ss == "ts" or ss == "TS" or
                ss == "vob" or ss == "VOB" or
                ss == "flv" or ss == "FLV" or
                ss == "m4v" or ss == "M4V" or
                ss == "mkv" or ss == "MKV"):

                result = re.findall(r'[a-zA-Z]{3,10}-\d+', vido_name)
                for fanhao in result:
                    fanhao = fanhao.upper()
                    # print(fanhao)
                    if fanhao not in list:
                        # print(fanhao)
                        list.append(fanhao.upper())
    # print(list)
    return list

# 提取需要检测的路径番号，并转换为大写
vido_list = avipath_nameid(r"e:\\")

# 提取索引路径内的番号，并转换为大写
data_list = avipath_nameid(r"D:\indexes")

# 对比两个列表中的番号，统计次数，如果次数大于1，则重复
for vido_name in vido_list:
    linshi_list = [s for s in data_list if vido_name in s]
    cishu = len(linshi_list)

    if cishu > 1:
        file = open("chongfu_logs.txt", 'a', encoding='UTF-8')
        print(vido_name, "文件重复")
        file.write(vido_name + "警告：文件重复，文件重复，文件重复\n")
        file.close()


input('Press Enter to exit...')