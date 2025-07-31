# 导入模块
import openpyxl

# 获取指定区间的数据

# 1、打开文件，生成文件对象
workbook = openpyxl.load_workbook("example.xlsx") # 这里文件名，也可以是文件路径，如：D:day/test.xlsx

# 2、获取活动表对象
sheet = workbook.active
print(f'当前活动表为：{sheet}')

# 3、得到指定区间内的所有单元格对象
cell = sheet['A1:A3'] # 得到 A1、A2、A3的单元格对象
print(f'所有单元格对象：{cell}') # 以元组形式返回

# 4、打印出所有单元格对象中的数据，这里直接使用for循环所有对象遍历出来
print('A1:A3的单元格数据依次为：')
for i in cell: # 这里嵌套了两个元组，需要两个for循环
    for x in i:
        print(x.value) # 得到单元格数据
