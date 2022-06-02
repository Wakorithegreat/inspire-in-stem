class Person :
    def __init__( self, _name , _age):
        self.name = _name
        self.age = _age

    def sayHi(self):
        print(" hello my name is " + str(self.name) + " and i am " + str(self.age) + " years old ")
person1 = Person("wakori",18)
person1.sayHi()
person2 = Person("ngaruiya",22)
person2.sayHi()