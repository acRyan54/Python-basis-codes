class Student(object):
    def __init__(self, name, gender, score = 100):
        self.name = name
        self.__gender = gender
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = 'male'
        elif gender == 'female':
            self.__gender = 'female'
