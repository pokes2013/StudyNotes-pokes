

import os
def name_JQ(str):


    # print("源文件："+str)
    str = str.replace(',', '')  # 去除逗号
    str = str.replace('“', '')  # 去除“”
    str = str.replace('”', '')  # 去除“”
    # str=''.join(str.split())            #去除空格
    wzzb = str.find('-')
    # print(wzzb)


    if wzzb != -1 :
        #分隔符之前的字符处理
        g_qian=str[0:wzzb+1]            #abc-
        # print("g_qian在这里"+g_qian)

        #分隔符之后的字符处理

        # g_hou_value=str[wzzb+1:wzzb+2]        # str="abc-1599999999bcdefg.mp4"
        # print("分隔符后的第一个字符："+g_hou_value)

        pokes=wzzb+2            ##-后第1个数字
        while pokes < 20:
        # print(pokes)
            pokes+=1
            g_hou = str[wzzb+1:pokes]
            chun = g_hou.isdigit()
            if chun == False:
                # print("不是纯数字了"+g_hou)
                break

        g_hou = str[wzzb + 1:pokes-1]
        zz=g_qian+g_hou
        print("处理结果："+"\n"+zz)
        f_XR = open("22222.csv", "a", encoding='UTF-8')
        f_XR.write(str+","+zz+"\n")
        f_XR.flush()
        f_XR.close()
    else:
        f_XR = open("22222.csv", "a", encoding='UTF-8')
        f_XR.write(str+","+str+"\n")
        f_XR.flush()
        f_XR.close()


def duqu(file):
    # file = "11111.csv"
    with open(file,"r", encoding="UTF-8") as f_lines:
    # with open(file,"r") as f_lines:
        for line_Y in f_lines:
            line_Y=line_Y.strip("\n")
            print(line_Y)
            z_name=name_JQ(line_Y)
            print(z_name)

duqu("pichuli/8100.csv")
