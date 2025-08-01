import os


def name_JQ(str):
    # print("源文件："+str)

    # 1、字符串过滤
    str = str.replace(',', '')  # 去除逗号
    str = str.replace('，', '')  # 去除“”
    # str=''.join(str.split())            #去除空格
    wzzb = str.find('-')
    # print(wzzb)

    # 如果没有“-”,则跳过处理

    # 分隔符之前的字符处理
    pokes1 = wzzb - 1
    while pokes1 < 20:
        # print(pokes1)
        pokes1 = pokes1 - 1
        g_qian = str[pokes1:wzzb]
        # print(g_qian)
        chun1 = g_qian.isalpha()
        if chun1 == False:
            print("不是纯字幕了")
            g_qian = str[pokes1+1:wzzb]
            break

    # g_qian = str[0:wzzb + 1]  # abc-
    # print("g_qian在这里"+g_qian)

    # 分隔符之后的字符处理

    pokes2 = wzzb + 2  # 横岗后第1.2.3....个数字
    while pokes2 < 20:
        # print(pokes)
        pokes2 += 1
        g_hou = str[wzzb + 1:pokes2]
        chun2 = g_hou.isdigit()
        if chun2 == False:
            # print("不是纯数字了"+g_hou)
            break

    g_hou = str[wzzb + 1:pokes2 - 1]
    zz = g_qian + "-" + g_hou
    print("处理结果：" + "\n" + zz)
    f_XR = open("data.csv", "a", encoding='UTF-8')
    f_XR.write(str + "," + zz + "\n")
    f_XR.flush()
    f_XR.close()


name_JQ("dwdd.umso-217.-h265.mp4")

# 2、读取源文件
# def duqu(file):
#     # file = "11111.csv"
#     with open(file, "r", encoding="UTF-8") as f_lines:
#         for line_Y in f_lines:
#             line_Y = line_Y.strip("\n")
#             print(line_Y)
#             z_name = name_JQ(line_Y)
#             print(z_name)
#
#
# duqu("hebing.csv")
