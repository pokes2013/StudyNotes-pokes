# # 仅支持.xls格式
# # （xlrd单元格数据类型表示：0：empty，1：string，2：number，3：date，4：boolean,5:error）
#
#
# import xlwt, xlrd
#
# data = xlrd.open_workbook(r"D:\code\python\06.excel操作\pokes-001.xls")
# print("打开文件", data)
#
# # 一、读取文件
#
# print("通过索引顺序获取第一个工作表", data.sheets()[0])
# print("获取全部sheet", data.sheets())
# print("返回book中所有工作表的名字", data.sheet_names())
# print(data.sheets()[0])  # 激活工作表对象
# print(data.sheet_by_index(0))  # 根据索引获取工作表,0表示第一个，以此类推
# print(data.sheet_by_name('Sheet1'))  # 根据名字sheetname（区分大小写）获取工作表
#
# # 查看共有多少个工作表
# print(len(data.sheet_names()))  # 返回所有工作表的名称组成的list的长度 3
# print(data.nsheets)  # 返回excel工作表的数量 3
#
# print("*" * 50)
#
# # 行操作
#
# sheet1 = data.sheet_by_index(0)  # 选择读取第一个工作表
# print(sheet1.nrows)  # 有效行数
# print(sheet1.row(0))  # 输出第一行数据，[text:'ID', text:'姓名', text:'性别', text:'年龄']
# print(sheet1.row(1))  # 输出第2行数据，返回该行单元格对象组成的列表
#
# print(sheet1.row_types(1))  # 获取单元格的数据类型，返回指定行数据的数据类型
#
# print(sheet1.row(1)[3])  # 获取单元格的数据类型，number:12.0
# print(sheet1.row(1)[2].value)  # 获取单元格value，男
# print(sheet1.row_values(1))  # 得到指定行单元格的值，['001', '张三001', '男', 12.0]
# print(sheet1.row_len(1))  # 得到单元格的长度
#
# print("*" * 50)
#
# # 操作excel列
#
# sheet1 = data.sheet_by_index(0)  # 选择读取第一个工作表
# print(sheet1.ncols)  # 有效列数
# print(sheet1.col(1))  # 该列单元格对象组成的列表
#
# print(sheet1.col(1)[2])  # 定位单元格获取值，1表示第二列，2表示第三行，查看字符类型
# print(sheet1.col(1)[2].value)  # 定位单元格获取值，1表示第二列，2表示第三行，获取值
# print(sheet1.col_values(1))  # 返回该列所有单元格的value组成的列表，其实就是将第二列的值组成一个列表
# print(sheet1.col_types(1))  # 获取该列单元格的数据类型 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# print("*" * 50)

# # 单元格操作
#
# sheet1 = data.sheet_by_index(0)  # 激活第一个工作表
# print(sheet1.cell(1, 2))  # 1是行，2是列，输出：text:'男' ，text是文本
# # 获取单元格数据类型
# print(sheet1.cell_type(1, 2))  # 1
# print(sheet1.cell(1, 2).ctype)  # 1
# # 获取单元格的值
# print(sheet1.cell(1, 2).value)  # 获取第二行，第三列单元格的值 男
# print(sheet1.cell_value(1, 2))  # 男
#
# print("*" * 150)
#
# # 一、写入数据
#
# # 第一步：创建工作簿
# wb = xlwt.Workbook(r"D:\code\python\06.excel操作\2019-CNY.xls")
# # 第二步：创建工作表
# ws = wb.add_sheet("CNY")
# # 第三步：填充数据
# ws.write_merge(0, 1, 0, 5, "2019年货币兑换表")
#
# # 写入货币数据
# data = (("Date", "英镑", "人民币", "港币", "日元", "美元"),
#         ("01/01/2019", 8.722551, 1, 0.877885, 0.062722, 6.8759),
#         ("02/01/2019", 8.634922, 1, 0.875731, 0.062773, 6.8601))
# for i, item in enumerate(data):
#     for j, val in enumerate(item):
#         ws.write(i + 2, j, val)
#
# # 创建第二个工作表
# wsImage = wb.add_sheet("image")
# # 写入图片
# wsImage.insert_bitmap("2021-07-01_172956.bmp", 0, 0)
# # 第四步：保存
# wb.save("2019-CNY.xls")


import re

text = "Hello 123 World 456"
pattern = re.compile(r"\d+")

matches = pattern.findall(text)
for match in matches:
    print(match)
