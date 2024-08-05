'''#creating a class

class Student:
    college_name="ABC college" #class attribute
    #constructor
    def __init__(self,name,marks):
        #self is reference to the current instance of the class(object)
        self.name=name #object attribute
        self.marks=marks
        print("adding new student in database...")

    def Welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks
        
        
#creating a object
        
s1=Student("nitish",88)
print(s1.name,s1.marks)

#attributes_- class attributes,  object attribute

print(s1.college_name)
#or-- print(Student.college_name)

s1.Welcome()
print(s1.get_marks())'''

#p1

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hi",self.name,"your avg score is:",sum/3)

    @staticmethod #decorator
    def hello():
        print("hello student")

s1=Student("tony",[98,97,96])
s1.get_avg()

s1.name="stark"
s1.get_avg() #we can change the attributes of an object

s1.hello()'''

 



