


import os

def file_list(path,extension=".mp4"):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    file_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in file_list if extension in s]
    return vido_list

# list=file_list(r"D:\code\python\05.函数的练习\05.99常用函数收藏\ceshioumei")
# print(list)

for video in file_list(r"D:\code\python\05.函数的练习\05.99常用函数收藏\ceshioumei"):
    # print(video)
    wzzb = video.find('.')
    # print(wzzb)
    om_name=video[wzzb+1:wzzb+9]
    print(om_name)

