__author__ = 'chenwei'
#coding:utf-8
class Student(object):
    def get_score(self):
        print self.score
        return self.score
    def set_socre(self,value):
        if not isinstance(value,int):
            raise ValueError("socre must be an integer!")
        if value <0 or value>100:
            raise ValueError("socre must between 0~100!")
        self.score = value

s=Student()
s.set_socre(100)
s.get_score()

class Student2(object):
    @property
    def score(self):
        print self._score
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("socre must be an integer!")
        if value <0 or value>100:
            raise ValueError("socre must between 0~100!")
        self._score = value

    @property
    def birth(self):
        print self._birth
        return  self._birth

    @birth.setter
    def birth(self,value):
        if not isinstance(value,int):
            raise ValueError("birth must be an integer!")
        if  value <1900 or value >2014:
            raise ValueError("birth must between 1900~2014!")
        self._birth = value

    @property
    def age(self):
        print "age:",2014 - self._birth

s2=Student2()
s2.score=60
s2.score
s2.birth = 1985
s2.birth
s2.age