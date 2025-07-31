import openpyxl

# 获取表数据的范围


workbook = openpyxl.load_workbook("example.xlsx") # 这里文件名，也可以是文件路径，如：D:day/test.xlsx

sheet = workbook['Sheet1']    #获取指定表对象
res = sheet.dimensions     #获取数据所占表格大小
print(res) # 输出结果：A1:B3