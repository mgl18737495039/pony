def ye():
    yield 1
    yield 2
    yield 3
    return "i love 白桑"
p = ye()

try :
     print(next(p))
     print(next(p))
     print(next(p))
     print(next(p))
except StopIteration as e:
    print(e)

list2=(i for i in range(100))
while True:
   try:
        p1=next(list2)
        print(p1)
   except:
       break