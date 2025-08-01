
# 确定“-”的位置

def hgwz(str):
    # print(str)
    wzzb = str.find('-')
    # print(wzzb)
#第三位是标准的忽略

#提取“-”右边4,5位是否是纯数字
    # name=str[7:8]
    # print(name4)

    var=8
    for var in range(8,20):
        name = str[7:var]
        # print(name)
        chun = name.isdigit()
        # print(chun)
        if chun == True:
            # print("尝试下一位")
            pass
        else:
            # print("不是纯数字了")
            break

    name = str[4:var-1]
    # print(name)

    str_zz=str[0:4]+name+".mp4"
    print(str_zz)

hgwz("@abcdss-15987654321bcdefg.mp4")






# 判断“-”右边4,5位是否是纯数字
#     生成第4位
#     wzzb04=str[wzzb+1:wzzb+4]
#     print(wzzb04)
#     chun04=wzzb04.isdigit()                 #判断第4位是f,还是t
#     print(chun04)
#     if  chun04 == True:                     第4位是t,则进入内测
#         wzzb02 = str[wzzb+1:wzzb+5]         #生成第5位
#         print(wzzb02)
#         chun02 = wzzb02.isdigit()           #判断第5位
#         print(chun02)
#         # 判断第5位
#         d5w = str[wzzb + 2:wzzb + 6]
#         if chun02 == True:
#
#             chun03 = wzzb03.isdigit()
#             print(wzzb03)
#         else:
#             pass
#     else:
#         pass






# shuzi_if=shuzi.isdigit()







