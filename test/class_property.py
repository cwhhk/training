__author__ = 'chenwei'
import time

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        __year = int(time.strftime('%Y',time.localtime(time.time())))
        if not isinstance(value, int):
            raise ValueError('birth must be an integer!')
        if value < __year - 100 or value > __year:
            raise ValueError('birth must between %s ~ %s' % (__year-100,__year))
        self._birth = value

    @property
    def age(self):
        __year = int(time.strftime('%Y',time.localtime(time.time())))
        return __year - self._birth


a = Student()
a.score = 60
a.birth = 1915
print time.strftime('%Y',time.localtime(time.time()))
print '%s,%s,%s' % (a.score,a.birth,a.age)