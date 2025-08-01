# 将文本内的名称转成一个列表

data = "data.txt"

with open(data, "r", encoding="UTF-8") as title:  #'r+'表示对文件是进行"读取和写入的模式"
    layertitle = title.read()
    layertitle_list = layertitle.split()  # 读取txt文件内容默认是str类型，此处将其分割成一个个元素形成列表
    print(layertitle)
    pokes = layertitle

# 创建文件

path = "D:/code/python/索引项目/suoyin/"  # 创建文件目录
for pokes in layertitle_list:
    f = open(path + pokes, "w", encoding="UTF-8")
    f.write(pokes)
