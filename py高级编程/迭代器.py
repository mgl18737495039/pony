from collections.abc import *

g=(x*x for x in range(5))
list=[1,1,1,1,1,1,1,1,2]
print(isinstance(list,Iterable))
print(isinstance(iter(list),Iterator))
list=iter(list)
print(next(list))