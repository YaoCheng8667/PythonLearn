'''
Test slice
切片
'''
print('===========================Test Slice==================================')
arr_int = [1,2,3,4,5,6,7,8,9,10]
tpl_int = (1,2,3,4,5,6)
str_demo = 'abcdefg'

'''
分片起始index为0可省略
'''
print(arr_int[:5])
print(arr_int[-5:])
print(arr_int[3:8])
print(arr_int[:])
print('---------------------')

'''
第二个冒号后表示间隔数
'''
# 前8个数每两个取一个
print(arr_int[:8:2])
print(arr_int[::3])

print('---------------------')
print(tpl_int[1:4])
print(str_demo[2:5])
print('sdfgsgsgsdgdfgs'[1:7])
