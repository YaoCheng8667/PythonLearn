from collections.abc import Iterable
'''
Test iteration
迭代
'''
print('============================Test iteration=============================')
'''
可迭代对象都是一个Iterable实例
'''
l = ['a', 'b', 'd', 'c']
print('t1',isinstance(l, Iterable))

'''
enumerate 可以遍历dict中的k,v键值对
'''
print('t2')
for i, v in enumerate(l):
    print(i,v)

'''
可以遍历多个tuple，返回值使用不同的变量进行接收
'''
print('t3')
l2 = [('a','aa','aaa'), ('b','bb','bbb'), ['c','cc','ccc']]
for s1, s2, s3 in l2:
    print(s1,s2,s3)