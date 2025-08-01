import os


def file_name_list(dir_path):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(filename)
    print(files_list)  # 所有文件的绝对路径


def file_path_lists(dir_path):
    """
        遍历dir路径下,所有文件.含子目录，最终结果显示绝对路径
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(parent, filename)  # 显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(file_path)
    # print(files_list)  # 所有文件的绝对路径
    return files_list


# file_name_list(r"F:\AV2021")


# # for files in files_list:
# #     print(files)
#
#
file_name_list(r"F:\AV2021")



