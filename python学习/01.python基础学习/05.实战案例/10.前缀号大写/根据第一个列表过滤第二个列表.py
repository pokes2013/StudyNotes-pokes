# coding=utf-8
# 声明两个列表变量

# list1 = ['1', '2', '3']  # 过滤掉1 2 3
# list2 = ['1', '2', '3', '4', '5', '6', '7']    #源数据
#
# # 根据第一个列表过滤第二个列表
# filter_data = [x for x in list2 if all(y not in x for y in list1)]
#
# # 在过滤前和过滤后打印列表数据
# print("第一个列表的内容:", list1)
# print("第二个列表的内容:", filter_data)
#
# # 输出:
# #
# # 第一个列表的内容: ['1', '2', '3']
# # 第二个列表的内容: ['4', '5', '6', '7']


# list1 = ["php", "python"]  # 需要的包含的字符串
# list2 = ["php", "python", "java", "nginx", "linux"]  # 源数据
# list3 = []  # 新建空列表用于存放生成的新数据
#
# for i in list1:
#     linshi_list = [s for s in list2 if i in s]
#     for a in linshi_list:
#         if a not in list3:
#             list3.append(a)
# print(list3)

# # 输出:
# ['php', 'python']

# for vido_file in geshi_list:
#     sxhvido_list = [s for s in all_list if vido_file in s]      # 生成一个新的列表，这个列表中包含了MP4等，是或的关系
#     for input_vido in sxhvido_list:
#         if input_vido not in shuaixuan_list:
#             if "-" in input_vido:  # 必须包含“-”
#                 if "欧美" or "三级" not in input_vido:  # 继续过滤
#                     # print(input_vido)  # 源文件路径


#声明混合数据列表
listData = ['linuxidc', 90, 9, 'com', 100, False, 22, True,  '1']

# 使用None和列表调用filter()方法
filteredData = filter(None,  listData)

#过滤数据后打印列表
print('过滤后的列表：')
for val in  filteredData:
    print(val)