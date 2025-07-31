# 导入模块
import openpyxl

# 获取单元格对象

workbook = openpyxl.load_workbook("example.xlsx")

# 方法 1：通过指定坐标，获得单元格对象，取得其中的数据;
sheet = workbook.active
# 通过坐标得到指定单元格对象
cell1 = sheet['A1']
cell2 = sheet['B3']
print(cell1,cell2) # <Cell 'Sheet1'.A1> <Cell 'Sheet1'.B3> ，代表A1和B3两个单元格对象

# 通过单元格对象得到单元格中的数据
res1 = cell1.value  # 获得A1中的数据
res2 = cell2.value  # 获得B3中的数据
print(res1,res2)    # 输出结果：姓名 24