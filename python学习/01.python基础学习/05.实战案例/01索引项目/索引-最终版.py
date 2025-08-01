import os

# # 将文本内的名称转成一个列表
data = "data.txt"  # 源文件
# #提取文件名
with open(data, "r", encoding="UTF-8") as f:
    for line in f:
        in_name = os.path.basename(line)
        print(in_name)
        # 创建文件
        path = "./suoyin/"
        bname = path + in_name
        out_name = bname.strip("\n")
        print(out_name)

        if os.path.exists(path):
            # 目录存在则创建文件
            print("文件创建成功")
            f = open(out_name, "w", encoding="UTF-8")
            f.write(out_name)

        else:
            # 不存在则先创建目录
            print("没有suoyin目录，正在创建")
            os.makedirs(path)
            f = open(out_name, "w", encoding="UTF-8")
            f.write(out_name)
