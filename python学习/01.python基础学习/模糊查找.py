#模糊匹配

import os
from collections import Counter


# data="pokes.txt"   #源文件
# pokes="pokes02.txt"
#
# # 提取文件名
# f = open(data, "r",encoding='utf-8')
#
# with open(data,"r", encoding="UTF-8") as file01:
#     for line01 in file01:
#         in_name = os.path.basename(line01)
#         # print(in_name)
#         out_name =in_name.strip('\n')
#         # print(out_name)
#         txt = open(pokes, "a",encoding='utf-8')
#         txt.write(out_name+"\n")
#
# # 将文件读取为一个列表
# file02 = open(pokes, "r",encoding='utf-8')
# a = [i for i in file02]
# # print(a)
# file02.close()
# list = dict(Counter(a))
# # print(list)
# print({key:value for key,value in list.items() if value > 1})



#需要导入Counter方法
from collections import Counter
List = [prdb-034,prdb-034,SOAV-007.mp4,1,2,SOAV-007.mp4,"python",prdb-034 加藤沙季.mp4,prdb-034 加藤沙季.mp4,"python"]
list = dict(Counter(List))
print({key:value for key,value in list.items() if value > 1})






# 提取前3个字符串



# 提取前4-7个字符串
