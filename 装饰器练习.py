# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func()
#         print('after')
#
#     return wrapper
#
#
# @decorator
# def hello():
#     print('hello world')
#     print('3+2={}'.format(3 + 2))


# hello()

class ClassDecorator(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, a=None, b=None, *args, **kwargs):
        print('请先依次输入两个数,我会给出你两数之和：')

        self.__fn(a, b)


@ClassDecorator
def sum1(a, b):
    a = int(input('输入第一个数，按回车结束：'))
    b = int(input('输入第一个数，按回车结束：'))
    c = a + b
    print('结果是:', end=' ')
    print(c)


sum1(4, 4)
