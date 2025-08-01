# 植入子目录然后过滤掉不包含横杠的，和不规则的


import os

# 分割文件名



def dx_name(str_name):


    # 定位分隔符
    wzzb = str_name.find('-')

    # 截取字母
    str_fenge_qian = str_name[:wzzb]

    # 转大写
    str_fenge_qian=str_fenge_qian.upper()

    # 截取分隔符后面的字符
    str_fenge_hou = str_name[wzzb:]

    # 拼接最终效果

    zz_name = str_fenge_qian+str_fenge_hou
    return zz_name

# dx_name("aaaaaabc-123_pokes01.mp4")



def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list





def update_name(houzhui):


    vido_list = file_list(os.getcwd(),houzhui)
    for vido in vido_list:
        # print(vido)
        xname = dx_name(vido)
        os.renames(vido,xname)


update_name("mp4")
update_name("MP4")
update_name("avi")
update_name("AVI")
update_name("KVM")
update_name("kvm")
