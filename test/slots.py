__author__ = 'chenwei'
#coding:utf-8
class Student(object):
    pass
s=Student()
s.name = "mike"
print s.name

def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s,type)
s.set_age(25)
print s.age

# s2=Student()
# s2.set_age(25)
# print s2.age
# 会报错
# Traceback (most recent call last):
#   File "E:/python_code/training/test/slots.py", line 16, in <module>
#     s2.set_age(25)
# AttributeError: 'Student' object has no attribute 'set_age'
def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,None,Student)
s2=Student()
s2.set_score(100)
print s2.score

class Student2(object):
    __slots__=('name','age')
s3=Student2()
s3.name = 'lily'
s3.age = '23'
# s3.score = '80'
print s3.name
print s3.age
# print s3.score
#会报错
# Traceback (most recent call last):
#   File "E:/python_code/training/test/slots.py", line 37, in <module>
#     s3.score = '80'
# AttributeError: 'Student2' object has no attribute 'score'

class GraduateStudent(Student2):
    __slots__ = ('score')
    pass
g = GraduateStudent()
g.score = 111
g.age = 11
print  g.score
print g.age