import os


# file_name = "ABP-834-C藤江史帆.mp4"
def fanhao_id(file_name):
    wzzb = file_name.find('-')  #获取分隔符的位置

    # 分隔符之前的字符处理
    numb1 = 0
    while numb1 < wzzb - 1:
        file_name_qz = file_name[numb1:wzzb]
        if (file_name_qz.isalpha()):  # 检测是不是纯字母isalpha()
            # print("纯字母是:" + file_name_qz)
            break
        numb1 += 1

    # 分隔符之后的字符处理

    numb2 = wzzb + 2
    # print(numb2)
    while numb2 < 10:
        file_name_hz = file_name[wzzb + 1:numb2]
        if not (file_name_hz.isdigit()):
            file_name_hz = file_name[wzzb + 1:numb2 - 1]
            # print("纯数字是",file_name_hz)
            break
        numb2 += 1

    fanhao = file_name_qz + "-" + file_name_hz
    # print(fanhao)
    return fanhao


# file_name = "ABP-834-C藤江史帆.mp4"
ffff=fanhao_id("ABP-834-C藤江史帆.mp4")
print(ffff)
