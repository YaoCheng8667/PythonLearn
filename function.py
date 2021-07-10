'''
Test for functions
函数
'''

'''
参数匹配测试：
    * 表示参数列表，可以接受任意数量的参数，内部可按照tuple方式处理接收的参数
    ** 表示dict形式的参数列表，内部按照dict方式进行处理。
    匹配顺序严格按照参数定义顺序
'''
print('=========================parameters matching===========================')
def multi_var_func(*args):
    for arg in args:
        print(arg)

def map_var_func(arg1,**arg):
    print(arg)

multi_var_func(1,3.5,'sdfsdfs')
arg_list = [1,2,3,4,5]
multi_var_func(*arg_list)

map_var_func(1,a='adsads',b='asdasdaf')
arg_map = {'aa':'aaaa','bb':'bbbb'}
map_var_func(1,**arg_map)

def func1(a,b,c=0,*arg_list,**arg_map):
    print('func1')
    for arg in arg_list:
        print(arg)
    print('--------')
    for arg in arg_map:
        print(arg)

func1(1,2,3,4,5,d=6,e=7)
func1(1,2,3,d=45,e=56)

'''
递归函数测试
'''
print('=========================Recursive function============================')
def fact(a):
    if a <= 1:
        return a
    else:
        return a * fact(a-1)

print(fact(4))

'''
函数作为返回值
'''
print('===========================Return a function===========================')
def lazy_sum(l):
    def sum():
        t = 0
        for x in l:
            t += x
        return t
    return sum

f_sum = lazy_sum([2,3,4,5])
print(f_sum)
print(f_sum())

'''
偏函数测试
'''
print('========================Partial function===============================')

from functools import partial

int2 = partial(int, base=2)
int16 = partial(int, base=16)

print(int2('101110001'))
print(int16('ABC'))