import os, sys


def dx_name(str_name):
    # 定位分隔符
    wzzb = str_name.find('-')
    # 截取字母
    str_fenge_qian = str_name[:wzzb]
    # 转大写
    str_fenge_qian = str_fenge_qian.upper()
    # 截取分隔符后面的字符
    str_fenge_hou = str_name[wzzb:]
    # 拼接最终效果
    zz_name = str_fenge_qian + str_fenge_hou
    return zz_name


def file_name_list(dir):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            file_path = os.path.join(parent, filename)  # 显示绝对路径
            # print(file_path)
            if file_path not in files_list:  # 这里有个去重复的判断
                files_list.append(file_path)
    # print(files_list)  # 所有文件的绝对路径
    return files_list


# file_name_list(r"D:\code\python\10.前缀号大写")


# 判断upname_logs.txt是否存在,如果存在则删除
if os.path.exists("upname_logs.txt"):
    os.remove('upname_logs.txt')

shuaixuan_list = []
geshi_list = [".mp4", ".MP4", ".AVI", ".avi", ".kvm", ".KVM"]

pathsss = r"F:\AV2021"
all_list = file_name_list(pathsss)
# all_list = file_name_list(os.getcwd())
for vido_file in geshi_list:
    sxhvido_list = [s for s in all_list if vido_file in s]  # 生成一个新的列表，这个列表中包含了MP4等，是或的关系

    list1 = ['欧美', '无码']        # 需要过滤的字符列表
    sxhvido_list = [x for x in sxhvido_list if all(y not in x for y in list1)]

    for input_vido in sxhvido_list:
        if input_vido not in shuaixuan_list:
            if "-" in input_vido:  # 必须包含“-”
                print("haha", input_vido)  # 源文件路径
