def fei(num):
    a=0
    b=1
    yield a
    yield b
    c=0
    while c<num:
        a,b=b,a+b
        yield b
        c+=1
for i in fei(100):
    print(i)