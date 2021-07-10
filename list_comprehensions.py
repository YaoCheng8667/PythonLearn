import os
'''
Test for list comprehensions
列表生成式
'''

'''
基础用法
'''
print('============================Basic usage================================')
l = [x * x for x in range(11)]
print(l)

'''
条件筛选与过滤
    For 前面是表达式，可以加if
    For 后面是过滤条件，不加if
'''
print('==========================Condition & Filter===========================')
l2 = [x * x for x in range(11) if x % 2]
l3 = [x * x for x in range(11) if x % 2 == 0]
print(l2,l3)
l3_1 = [x * x if x % 2 else -x * x for x in range(9)]
print('L3_1',l3_1)

'''
多级For循环
'''
print('==============================Multi-For================================')
l4 = [m + n + k for m in 'asd' for n in 'zxc' for k in 'qwe']
print('L4',l4)

'''
遍历目录中所有文件名用法
'''
print('==============================File iteration===========================')
files = [d for d in os.listdir('.')]
print(files)

'''
多个变量生成list
'''
print('==============================Multi-Var================================')
mp = {'a' : 1, 'b' : 2, 'c' : 3}
l5 = [k + ' = ' + str(v) for k , v in mp.items()]
print(l5)
