# 集合的交集

import re, os


# 遍历文件及子文件

def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


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
        是不是和下面的重复了
    """
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        if "mp4" or "mkv" or "avi" in vido_name:
            result = re.findall(r'[a-zA-Z]{2,10}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # print(fanhao)
                if fanhao not in list:
                    # print(fanhao)
                    list.append(fanhao.upper())
    # print(list)
    return list


def avipath_nameid_bt(inpath):
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        if "mp4" or "mkv" or "avi" in vido_name:
            result = re.findall(r'[a-zA-Z]{2,10}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # print(fanhao)
                if fanhao not in list:
                    # print(fanhao)
                    list.append(fanhao.upper())
    # print(list)
    return list



# 得到两个集合
bt_list = avipath_nameid(r"E:\avfilm")  # 需要检查的目录
data_list = avipath_nameid(r"D:\indexes")

# 将集合转换为列表
bt_list = set(bt_list)
data_list = set(data_list)

#求出交集，会用到intersection函数
result = bt_list.intersection(data_list)
print(result)
