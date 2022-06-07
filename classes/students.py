#!/usr/bin/python
###############
#student
#name :john wakori
# date : 23/5/20
################
class Student:
    def __int__(self,name,hobby,year_of_birth):
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth

    def greetStudent(self):
        print("hello from student" + str(self.name) + "hobby :" + str(self.hobby) + "years old :" + str(self.year_of_birth))