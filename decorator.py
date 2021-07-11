'''
Decorator : 装饰器
'''
import time
import functools
print("========================Log Decorator==================================")

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s : In function (%s)' % (text,func.__name__),time.asctime(time.localtime(time.time())))
            return func(*args,**kw)
        return wrapper
    return decorator

'''
@log('DEBUG') 表示调用log('DEBUG')会返回一个函数，该函数接收一个func作为参数，并返回一个包装后的func
'''
@log('DEBUG')
def test():
    print('Test func')

print(test.__name__)
test()