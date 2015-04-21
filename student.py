# student.py
# Name: Christopher Salazar
# Date: 04/20/2015


class Student:

    def __init__(self,name,stuID,gpa,grade,time):
        self.__name=name
        self.__stuID=stuID
        self.__gpa=gpa
        self.__grade=grade
        self.__time=time
        
    def set_studentID(self,stuID):
        self.__stuID=stuID

    def set_gpa(self, gpa):
        self.__gpa=gpa

    def set_grade(self, grade):
        self.__grade=grade
        
    def set_time(self, time):
        self.__time=time

    def get_name(self):
        return self.__name
        
    def get_studentID(self):
        return self.__stuID

    def get_gpa(self):
        return self.__gpa

    def get_grade(self):
        return self.__grade

    def get_time(self):
        return self.__time
