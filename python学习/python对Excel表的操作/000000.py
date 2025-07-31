for i in range(1, 10):      # 外层循环控制行数
    for j in range(1, i+1):  # 内层循环控制每行的表达式
        print(f"{j}×{i}={i*j}", end="\t")  # 使用制表符对齐
    print()                  # 每行结束后换行