from collections.abc import *
class goods():
    def __init__(self,_args):
        self.args=_args
        self.index=0
    # def __iter__(self):
    #     return self
    def __next__(self):
        if self.index<len(self.args):
            result=self.args[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration("引发越界")
g=goods(["xinx","zhengzhou","xiaobai"])

print(isinstance(g,Iterator))
try:

    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as g:
    print(g)



