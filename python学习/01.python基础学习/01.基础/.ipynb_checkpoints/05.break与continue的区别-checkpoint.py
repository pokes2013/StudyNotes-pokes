#04.break与continue的区别
# 详情可查看：https://blog.csdn.net/qq_48374573/article/details/117231318
# break用于跳出一个循环体或者完全结束一个循环，不仅可以结束其所在的循环，还可结束其外层循环。
# continue语句的作用是跳过本次循环体中剩下尚未执行的语句，立即进行下一次的循环条件判定，可以理解为只是中止(跳过)本次循环，接着开始下一次循环。



while True:    #True无条件放行
    answer=input('你的腿怎么样？还能坚持吗？')
    if answer=='y':
        print('加油')
    else:
        print('不能，退赛')
        break                    #终止



print('-----------------------------')

circle=0
for i in range(1,11):
    answer=input('能跑吗？')
    if answer!='y':               #取反，不等于y
        continue                  #continue语句只结束本次循环,而不是终止整个循环的执行
    circle+=1
print('一共跑了',circle,'圈')