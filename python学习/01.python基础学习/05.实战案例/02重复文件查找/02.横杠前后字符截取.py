import os
import re


# 适合类似abcd-123,横杠后面有3个数字的

def name_jq(str, number=3):
    wzzb = str.find('-')  # 确定 “-” 在字符串中的位置
    # print(wzzb)
    list_srt = str.split('-')
    # print(list_srt[2])
    bcp_name = list_srt[0] + "-" + list_srt[1]  # 从列表中拼接字符串
    # print(bcp_name)

    # 提取第7位
    wzzb01 = wzzb + 1
    h1w = wzzb01 + 4
    shuzi = str[wzzb01:h1w]
    # print(shuzi)
    shuzi_if = shuzi.isdigit()
    # print(shuzi_if)
    # print(str[3:7])


    # 判断“-”后面是不是纯数字
    shuzi_if is "True"
    jqwz = wzzb + number + 2
    # print(jqwz)
    zz = bcp_name[0:jqwz]  # 最终数据zz
    print(zz)

    shuzi_if is not "True"
    jqwz = wzzb + number + 1
    # print(jqwz)
    zz = bcp_name[0:jqwz]  # 最终数据zz
    # print(zz)


name_jq("DV-1599bcdefg.美里有紗")

# str.isdigit()     #仅可判断非负整数,不可用，
# AttributeError: 'int' object has no attribute 'isnumeric'

# str.partition(str)
# 如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
