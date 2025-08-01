


# 读取依据文件，最好是excel01，得到字符串01
#
# # 01判断包含桃花族“hd800”字符
#
# def hd800(name01):
#
# # name01 = "hhd800.com@SABA-799.mp4"   #遇到这种直接截取@右边的
#
#     str01 = name01.split("@")
#     # print(str01[1])
#     str01 = str01[1].split(".")
#     print(str01[0])
#
# hd800("hhd800.com@SABA-799.mp4")
#
# # 02.判断包含桃花族“蜂鳥”字符
#
# def fengniao(name02):
#     # name02 = "@蜂鳥@FENGNIAO131.VIP-SABA-670_2K-1.mp4"    #截取VIP右边，和2K左边
#     str02 = name02.split("VIP-")
#     # print(str02)
#     str02[1]
#     str02 = str02[1].split("_")
#     # print(str02)
#     print(str02[0])
#
# fengniao("@蜂鳥@FENGNIAO131.VIP-SABA-670_2K-1.mp4")
#
# # 03.判断包含桃花族[Thz.las]字符
#
# def thz(name03,zifu03):
# # name03 = "[Thz.las]vrtm-295.mp4"            #截取]的
#     bh03 = zifu03 in name03
#     if bh03 == True:
#         str03 = name03.split("]")
#         # print(str03[1])
#         str03 = str03[1].split(".")
#         print(str03[0])
#     else:
#         print("文件"+name03+"名称中：不包含字符串[Thz.la]")
#
# thz("[Thz.las]vrtm-295.mp4","[Thz.las]")


# 04.类似OFJE多集的过滤


def ofje(name04,zifu04=10):
    # name04="OFJE-129-3.-xk264-003.-xk264_1.mp4"
    bh04 = "ofje-" in name04                             #判断小写的
    # print(bh04)
    if bh04 == True:
        str04 = name04[0:zifu04]
        print(str04)
        print("文件：" + name04 + "名称中：包含字符串小写ofje")
    else:
        bh04 = "OFJE-" in name04                         #判断大写的
        if bh04 == True:
            print("文件：" + name04 + "名称中：包含字符串大写OFJE")
            str04 = name04[0:zifu04]
            print(str04)
            # str04 = str04[1].split(".")
            # print(str04[0])
        else:
            print("文件："+name04+"名称中：不包含字符串ofje")

ofje("OFJE-129-3.-xk264-003.-xk264_1.mp4")





# 99.普通包含abc-123大小写的处理

# 待续




#
#思路：
# str01 = "abc-123"
#
# # 读取依据文件，最好是excel02，得到字符串02
#
#
# str02 = "abc-123"
#
#
# #判断 str01  是否包含  str02
#
# pokes = str01 in str02
# print(pokes)
#
# if pokes == True:
#     print("发现重复：",str01)
# else:
#     print("没有发现重复")
#
#
#
#
#
#
