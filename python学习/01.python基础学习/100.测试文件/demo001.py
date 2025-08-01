# 解决方案
# ◆列表
# 列表解析：[x for x in data if x>=0]
# filter函数：filter(lambda x:x>=0,data)
# ◆字典
# 字典解析：{k:v for k,vind.items()ifv>90}
# ◆集合
# 集合解析：{x for x in s if x%3==0}

# 列表解析


l = ["dadsdsd-欧美", "dww三级", "yututy香港", "bcvbb国产", "ewqeewq麻豆", "tyvcv韩国", "asa欧洲", "dwdwd素人", "trhhtr"]
print(l)

r = [x for x in l if "欧美" not in x]
print(r)

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


# avipath_nameid(r"F:\AV2021\41-已筛选")

# vido_list = avipath_nameid(os.getcwd())  # 需要检查的目录
# vido_list = avipath_nameid(r"F:\AV2021\41-已筛选")  # 需要检查的目录
vido_list = avipath_nameid(r"F:\")  # 需要检查的目录
data_list = avipath_nameid(r"D:\indexes")
# pokes_list = [s for s in data_list if instr in s]  # 找出所有搜索结果
for vido_name in vido_list:
# "欧美" not in
    linshi_list = [s for s in data_list if vido_name in s]
cishu = len(linshi_list)
# print(cishu)

if cishu == 1:
    file = open("chongfu_logs.txt", 'a', encoding='UTF-8')
print(vido_name, "文件重复")
file.write(vido_name + "警告：文件重复，文件重复，文件重复\n")
file.close()

input('Press Enter to exit...')
