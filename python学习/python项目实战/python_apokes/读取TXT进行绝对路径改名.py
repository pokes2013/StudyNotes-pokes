import os

"""
此程序是一个更改文件名的程序。将文本中的绝对路径的文件名，字母改为小写
"""


def txt_list():
    """
    逐行读取txt文件，将其变为一个列表
    """
    list_vido_any = []
    list_vido_any.clear()
    with open(r'D:\systemdoc\desk\666\data.txt', 'r', encoding='UTF-8') as file:
        # print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            list_vido_any.append(line)
    # print(list_vido_any)
    return list_vido_any


for old_name in txt_list():
    # 得到源文件名和路径
    print(old_name)

    # 替换其中的文本
    new_name = old_name.replace("[动漫][动漫]", "[动漫]")
    #执行修改
    os.renames(old_name, new_name)
    print("更改成功：\n" + old_name + "\n" + new_name + "\n"*2)

    # new_name=pass






    #
    # now_name = old_name.lower()
    # # print(now_name)
    # os.renames(old_name, now_name)
    # print("更改成功：\n" + old_name + "\n" + now_name + "\n"*2)
