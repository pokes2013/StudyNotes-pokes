# srcfile 需要复制、移动的文件
# dstpath 目的地址

import os
import shutil
from glob import glob


def mymovefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))


src_dir = "./"
dst_dir = "./suoyin/"  # 目的路径记得加斜杠
src_file_list = glob(src_dir + "*")  # glob获得路径下所有文件，可根据需要修改
for srcfile in src_file_list:
    mymovefile(srcfile, dst_dir)  # 移动文件
