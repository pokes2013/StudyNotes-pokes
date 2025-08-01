import os


def vido_any(kuozhan_list,windows_path=os.getcwd()):
    files_list = os.listdir(windows_path)  # 当前目录所有文件的序列

    list_vido_any = []
    for kuozhan_name in kuozhan_list:

        vido_list_xx = [s for s in files_list if kuozhan_name in s]  # 这里有个bug,不支持大写扩展名
        for filename_xx in vido_list_xx:
            list_vido_any.append(filename_xx)

        kuozhan_name_up = kuozhan_name.upper()  # 修复这个bug
        vido_list_up = [s for s in files_list if kuozhan_name_up in s]  # 转大写搜索，再次写入列表中
        for filename_dx in vido_list_up:
            list_vido_any.append(filename_dx)

    print(list_vido_any)
    return list_vido_any




def up_name(vido_name):
    wzzb = vido_name.find('-')
    # 截取字母
    str_fenge_qian = vido_name[:wzzb]
    # 转大写
    str_fenge_qian=str_fenge_qian.upper()
    # 截取分隔符后面的字符
    str_fenge_hou = vido_name[wzzb:]
    # 拼接最终效果
    zz_name = str_fenge_qian+str_fenge_hou
    # print(zz_name)
    return zz_name

# 调用

kuozhan_list=[".mp4", ".avi"]
vido_list_mp4 = vido_any(kuozhan_list)
# print(vido_list_mp4)
for vido_name in vido_list_mp4:
    result = up_name(vido_name)
    print(result)
    os.renames(vido_name, result)
