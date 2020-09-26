## 有用的函数
# enumerate() 
函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。   
eg: 
```
seq = ['one', 'two', 'three']  
for i, element in enumerate(seq):  
    print(i, element)  
0 one  
1 two  
2 three  
```
# zip()
函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
```
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
## [(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
## [(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
## [(1, 2, 3), (4, 5, 6)]
```


# range()
range(start, stop[, step])
```
# 输出偶数   
list(range(0, 10, 2))
```