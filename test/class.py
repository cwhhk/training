__author__ = 'chenwei'
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%s' % (self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            print 'A'
        elif self.score >= 60:
            print 'B'
        else:
            print 'C'

bart = Student('Bart Simpson',60)
bart.print_score()
bart.get_grade()