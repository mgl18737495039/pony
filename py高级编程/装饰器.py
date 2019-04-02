def check(fun):
    def ck():
        user =input('输入账户名')
        if user=='zzy':
            fun()
        else:
            print("该账户未注册")
    return ck
@check
def func():
    print("校验成功")
print(func.__name__)
