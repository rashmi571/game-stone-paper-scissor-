
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__ (self,name,age,marks):
        super().__init__ (name,age)
        self.marks=marks
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)
        
    

s=Student("Raashmi",19,100)
s.show()
                     