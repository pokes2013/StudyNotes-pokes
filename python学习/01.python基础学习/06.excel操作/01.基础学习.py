import os
import openpyxl

path = r"D:\code\python\06.excel操作"
os.chdir(path)  # 修改工作路径

# 创建工作簿和默认的工作表
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'pokes01'  # 创建表并指定名称，如果不写默认创建表名sheet
workbook.save('pokes.xlsx')  # 保存为pokes.xlsx的文档
