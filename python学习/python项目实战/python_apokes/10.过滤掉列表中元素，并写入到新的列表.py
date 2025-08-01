def guolvhaha(lists):
    """
    过滤掉一个列表中的非法字符
    """
    # lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye三级.123456"]
    ffstr_list = ["欧美", "国产", "韩国", "香港", "$"]  # 将这些视为非法字符
    nowlist = []
    for vido in lists:
        # print(vido)
        for ffstr in ffstr_list:  # 遍历出需要过滤的字符
            if (ffstr in vido) or ("-" not in vido):  # 满足一个条件就跳过本次循环
                # print(vido,"buguize")
                continue
            else:
                # print(vido)
                if vido not in nowlist:
                    nowlist.append(vido)
                    return nowlist


lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye.123456"]
heihei = guolvhaha(lists)
print(heihei)
