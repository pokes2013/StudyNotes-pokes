# 导入模块
import openpyxl

# 1、打开文件，生成文件对象
workbook = openpyxl.load_workbook("example.xlsx") # 这里文件名，也可以是文件路径，如：D:day/test.xlsx
# 注意：该文件必须存在，不然会报错
# 2、获取活动表对象
sheet = workbook.active
print(f'当前活动表为：{sheet}')

# 3、获取所有行中的数据
data1 = sheet.rows
print(f'所有行对象：{data1}')
# 通过for循环将每行的单元格对象遍历出来
for i in data1:
    print(i)
    for x in i:
        print(x.value) # 打印所有单元格数据

print('==============')
# 4、获取所有列中的数据
data2 = sheet.columns
print(f'所有列对象{data2}')
# 通过for循环将每行的单元格对象遍历出来
for i in data2:
    print(i)
    for x in i:
        print(x.value) # 打印所有单元格数据
