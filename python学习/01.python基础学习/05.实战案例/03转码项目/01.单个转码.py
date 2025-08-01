#学会如何在python调用cmd命令文件

import os,sys


# 输入要转换的文件

def zhuanma(input):
	dir = os.path.dirname(input) 			#提取所在目录
	namekzm = os.path.basename(input) 		#提取文件名含扩展名，不包含路径
	name = os.path.splitext(input)[0]		#提取路径和文件名，不含扩展名
	output = name+"_ok.mp4"
	compress = "ffmpeg -i {} -vcodec h264 -b:v 0 -s 1280x720 {}".format(input,output)      #python调用cmd命令方法
	isRUN = os.system(compress)
	print("*"*60)
	print(input+'-转换成功')


#调用

s = "E:/LOL视频/测试视频/霞五杀001.mp4"
zhuanma(s)
