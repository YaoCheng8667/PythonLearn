'''
Test class
'''

'''
__slots__:
    类成员__slots__定义的列表表示了该类可以定义及访问的属性
@property:
    1. 定义一个函数作为属性，并作为其getter方法，同时生成一个 属性名.setter 的装饰器，
    重载其单参同名方法可以作为setter方法。
    2. property函数名不可与其维护的私有变量同名，私有变量也必须位于__slots__中，否则会报错
__str__():
    定义str(Student)的返回，也即print(student)打印格式
'''
from typing import Iterable


print('========================Test case : Class Student======================')
class Student(object):
    __slots__ = ['name','age','_score']
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return 'Name : ' + str(self.name) + \
               '\nAge : ' + str(self.age) + \
               '\nScore : ' + str(self._score)

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, x) -> None:
        if not isinstance(x,int):
            raise ValueError('score must be an integer')
        if x < 0 or x > 100:
            raise ValueError('score must between 0 and 100')
        self._score = x
    
s = Student()
s.name = 'Xiaoming'
s.age = 15
print(s.name,s.age)
# s.sex = 'male' # 报错，因为 sex 没有出现在__slots__列表中
s.score = 88
s.score = 17
print(s.score)
print(s)
# s.score = -3  # 报错，因为 score 未满足 0 ~ 100 的条件

'''
若一个对象可以像 list 或 tuple 那样可被迭代，需要实现__iter__()函数。
__iter__(self): 
    返回一个可迭代对象，该对象实现了__next__()方法，每次 for x in ... 时，
    调用__next__() 返回一个对象。
__getitem__(self,n):
    返回索引为 n 的元素，n也可能是一个切片，实现之后可以采用 fib[n] 或 fib[1:5]
    等方式返回对应位置的元素或list。
'''
print('=======================Test case : Class Fib===========================')
class Fib(object):
    def __init__(self, num = 20) -> None:
        super().__init__()
        self._a = 0
        self._b = 1
        self._num = num

    def __iter__(self):
        return self

    def __next__(self):
        if(self._num <= 0):
            raise StopIteration()
        self._a, self._b = self._b, self._a + self._b
        self._num -= 1
        return self._a
    
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for i in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            st = n.start
            ed = n.stop
            if st is None:
                st = 0
            l = []
            for i in range(ed):
                if i >= st:
                    l.append(a)
                a, b = b, a + b
            return l
        
fib = Fib(15)
print(isinstance(Fib,Iterable))
for x in fib:
    print(x)

print('fib[5] : %d ' % fib[5])
print('fib[2:6] :', fib[2:6])
print('fib[:10] :', fib[:10])

'''
__call__(self,*):
    表示这个类对应的对象为一个可调用的对象，可以直接使用 () 调用其__call__()方法。
__getattr__(self, attr_name):
    表示获取该对象的某一个属性，只有当其他属性均未找到时才会去调用。
'''
print('=====================Test case : Class Printer=========================')
class Printer(object):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'my_printer'
    
    def __call__(self, *args, **kwds) -> None:
        for msg in args:
            print(msg)
        for msg in kwds:
            print(kwds)
        # return super().__call__(*args, **kwds)
    def __getattr__(self, attr_name: str) -> str:
        return 'Attr: (' + attr_name + ') not defined'
        
p = Printer()
p('this is a msg', 1, me='yc')
print(p.name)
print(p.sex)
