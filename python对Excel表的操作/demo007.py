# 导入模块
import openpyxl

# 1、打开文件，生成文件对象
workbook = openpyxl.load_workbook("example.xlsx") # 这里文件名，也可以是文件路径，如：D:day/test.xlsx
# 注意：该文件必须存在，不然会报错
# 2、获取活动表对象
sheet = workbook.active
print(f'当前活动表为：{sheet}')

# 3、得到指定列中所有单元格对象
cell = sheet['A:B'] # 得到第A、B两列中所有的单元格对象
print(f'所有单元格对象：{cell}') # 以元组形式返回
# 4、打印出所有单元格对象中的数据，这里直接使用for循环所有对象遍历出来
print('A列和B列所有单元格数据依次为：')
for i in cell: # 这里嵌套了两个元组，需要两个for循环
    for x in i:
        print(x.value) # 得到单元格数据
