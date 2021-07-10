'''
Filter 过滤器
'''
print('===========================Test filter=================================')
def is_odd(x):
    return x % 2 == 1

l_odd = tuple(filter(is_odd,[12,44,3,35,32,7,88,79]))
print(l_odd)
l_even = tuple(filter(lambda x : x % 2 == 0,[12,44,3,35,32,7,88,79]))
print(l_even)

