# import re

def name_JQ(str):
    print("源文件：" + str)
    str = str.replace(',', '').replace('，', '').replace(' ', '').replace('VIP-', '')

    print("特殊字符过滤:" + str)

    # str=''.join(str.split())            #去除空格
    wzzb = str.find('-')
    # print(wzzb)

    # 如果没有“-”,则跳过处理

    # 分隔符之前的字符处理
    pokes01 = 0
    while pokes01 < wzzb - 1:
        str_ZM = str[pokes01:wzzb]
        # print(chun_ZM)
        if (str_ZM.isalpha()):  # 检测是不是纯字母isalpha()
            print("纯字母是:" + str_ZM)
            # print(str_ZM)
            break
        pokes01 += 1

    # 分隔符之后的字符处理

    # g_hou_value=str[wzzb+1:wzzb+2]        # str="abc-1599999999bcdefg.mp4"
    # print("分隔符后的第一个字符："+g_hou_value)

    pokes02 = wzzb + 2
    while pokes02 < 30:
        str_SZ = str[wzzb + 1:pokes02]
        # print(str_SZ)
        if (str_SZ.isdigit()) == False:
            # print("不是纯数字了"+str_SZ)
            str_SZ = str[wzzb + 1:pokes02 - 1]
            print("纯数字是:" + str_SZ)
            break
        pokes02 += 1
    str_SZ = str[wzzb + 1:pokes02 - 1]

    # 整合显示结果

    zz = str_ZM + "-" + str_SZ
    print("处理结果：" + zz)
    # f_XR = open("data.csv", "a", encoding='UTF-8')
    # f_XR.write(str + "," + zz + "\n")
    # f_XR.flush()
    # f_XR.close()


name_JQ("12312321abcd-123411-dwjidwjwid")
