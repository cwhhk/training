__author__ = 'chenwei'
#coding:utf-8
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name:%s)'%self.name
#     __repr__ = __str__
# print Student('Michael')
#
# s=Student("Jack")
# print s

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def next(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a >10000:
#             raise StopIteration()
#         return self.a
#     def __getitem__(self, item):
#         if isinstance(item,int):
#             a,b = 1,1
#             for x in range(item):
#                 a,b=b,a+b
#             return a
#         if isinstance(item,slice):
#             start = item.start
#             stop = item.stop
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x >=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
#
# for n in Fib():
#     print n
# print Fib()[5]

# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#         if attr == 'age':
#             return lambda : 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# s = Student()
# print s.name
# print s.score
# print s.age()
# print s.abc

# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path,path) )
#     def __str__(self):
#         return self._path
# print Chain().status.user.timeline.list

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __call__(self):
#         print("My name is %s." % self.name)
#
# callable(Student(11))
# callable(max)
# callable([1,2,3])
# callable(None)
# callable("string")


# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#     def __call__(self,name):
#         self._call_name = self
#         self._name = name
#         return Chain('Get %s/%s' % (self._call_name,self._name) )
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path,path) )
#     def __str__(self):
#         return self._path
# print Chain().users('michael').repos

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def getpath(self):
        return self._path

    def _setpath(self,path,f=0):
        k=self._path.find('GET');
        if(not f):
            if(k==0):
                self._path=('%s/%s' % (self._path, path))
            else:
                self._path=('GET %s/%s' % (self._path, path))
        else:
            self._path=('%s/:%s' % (self._path, path))

    def __getattr__(self, path):
        self._setpath(path)
        return self

    def __str__(self):
        return self._path

    def __call__(self,path=''):
        self._setpath(path,1)
        return self

    __repr__=__str__

print Chain().users("Macheal").repo