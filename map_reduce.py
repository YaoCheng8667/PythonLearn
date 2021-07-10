'''
Map reduce
'''

'''
map(func,list) : 将传入列表list中的每个元素作为参数传给func执行，返回func返回值构成的新列表
'''
print('===========================Test Map====================================')
def f(x):
    return x * x

r = map(str, [1,2,3,4,5])
r2 = [x * x for x in [1,2,3,4,5]]
for x in r :
    print(x)
for x in r2:
    print(x)

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
print('===========================Test Reduce=================================')
from functools import reduce

l = [5,4,6,7,3]

def fn(x1,x2):
    return x1 * 10 + x2

print(reduce(fn,l))

