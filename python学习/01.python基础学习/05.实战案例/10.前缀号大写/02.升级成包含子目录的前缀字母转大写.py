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
geshi_list = [".mp4", ".MP4", ".AVI", ".avi", ".kvm", ".KVM", "-"]
all_list = file_name_list(os.getcwd())
for vido_file in geshi_list:
    sxhvido_list = [s for s in all_list if vido_file in s]  # 生成一个新的列表，这个列表中包含了MP4等，是或的关系

    list1 = ['欧美', '无码', '韩国', '三级', '蒂法', '3D', '动漫', '国产']  # 需要过滤的字符列表
    sxhvido_list = [x for x in sxhvido_list if all(y not in x for y in list1)]

    for input_vido in sxhvido_list:
        if input_vido not in shuaixuan_list:
            input_vido_fg = input_vido.split('\\')  # 把路径切片
            # print(input_vido_fg)
            input_vido_fg_zhys = input_vido_fg[-1]  # 列表的随后一个元素
            zhh = dx_name(input_vido_fg_zhys)  # 调用上面的函数处理大小写转换
            del (input_vido_fg[-1])  # 删除最后一个元素
            input_vido_fg.append(zhh)  # 添加转换后大写的元素到列表最后
            # print(input_vido_fg)

            newname_out_path = "\\".join(input_vido_fg)  # 把列表中的元素合并成一个路径
            os.renames(input_vido, newname_out_path)

            if input_vido != newname_out_path:
                print("更改成功:", input_vido)
                print("更改结果:", newname_out_path + "\n")
                f = open('upname_logs.txt', "a", encoding='UTF-8')
                f.write(input_vido + "\n" + newname_out_path + "\n" + "\n")
                f.close()
