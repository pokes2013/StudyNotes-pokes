# 学会如何在python调用cmd命令文件

import os, sys


# 输入要转换的文件

def zhuanma(path, fbl):
    # 提取源文件绝对路径
    oldlist = os.listdir(path)
    logs = path +'\log.txt'
    print(logs)

    # 用for循环遍历出每个文件的名称进行拼接
    for i in oldlist:
        input = path + '/' + i                   # 拼接输入文件E:/ceshi/霞五杀003.mp4
        name = os.path.splitext(input)[0]        # 不带扩展名的路径，例如：E:/ceshi/霞五杀003
        output = name + '_OK.mp4'                # 拼接最终变成：E:/ceshi/霞五杀003_OK.mp4

        # 转码系统
        compress = "ffmpeg -i {} -vcodec h264 -b:v 0 -s {} {}".format(input, fbl, output)  # python调用cmd命令方法转码
        isRUN = os.system(compress)
        print("*" * 100)  # 分割线
        print(input + '-转换成功')  # 输出转换成功的提示

        # 日志系统，日志文件在视频目录中
        file = open(logs, 'a', encoding='UTF-8')
        file.write(input + "\n")
        file.close()


# 分辨率选项
a = "720x404"
b = "960x540"
c = "1280x720"
d = "1920x1080"

# 路径
# input_Path = r"E:\ceshi"  # 注意引号
zhuanma("r"+E:\ceshi, a)
