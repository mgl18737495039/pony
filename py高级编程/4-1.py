import types
class student():
    contry="China"
    __slots__ = ("age","name","classs","updata_classs")
    def __init__(self,age):
        self.age=age

stu1=student(13)
stu1.name='mgl'
stu1.classs='一年级'

def updata_classs(self,classs):
    self.classs=classs
    return self.classs
stu1.updata_classs=types.MethodType(updata_classs,stu1)
print(stu1.classs)
print(stu1.updata_classs('二年级'))

student.contry='日本'
student.contry_s='东京'
print(stu1.contry,stu1.contry_s)

@classmethod
def upda_c(cls,con,con_s):
    cls.contry=con
    cls.contry_s=con_s
student.upda_c=upda_c
student.upda_c('中国','河南')
print(stu1.contry,stu1.contry_s)