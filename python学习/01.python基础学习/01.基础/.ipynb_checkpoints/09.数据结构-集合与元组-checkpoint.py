# 集合
## 集合就好似离了婚得字典，它只有键，没有值。

s={'41','42','43'}
print(s)

# 注意：需要注意得是他是没有顺序得，不是说放在第一个就是1；



# 添加
s.add('34')
print(s)

# #删除
s.remove('43')
print(s)
#
# #遍历
s={'41','42','43'}
for item in s:
    print(item)

#获取里面单个得元素
s={'41','42','43'}
lst=list(s)  #将集合转成列表,转换之后就有索引了
print(lst[0])   #结果是随机得，因为他是无序得

#元组
# 他和集合很相似，但是他是加了锁得，不能新增、修改、删除，只能查看。也叫不可变序列
tuple_size=('41','41','43','42',)
print(tuple_size)   #我们发现可以运行，那么也就是说元组可以放重复得数据   # 知识点：列表和元组得’键‘可以放重复得数据，但是集合和字典是不允许重复得！

#通过列表获取元素
# print(tuple_size[0])

#遍历
for item in tuple_size:
    print(item)

总结：