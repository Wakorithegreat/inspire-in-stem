# writing employees name and salary
class Employee :
    def __init__(self ,  _name ,  _salary):
        self.name = _name
        self.salary = _salary
    def sayHi(self):
        print(" name : "  + str(self.name) +  "salary : " + str(self.salary))
employee1 = Employee("james" , 25000)
employee1.sayHi()
