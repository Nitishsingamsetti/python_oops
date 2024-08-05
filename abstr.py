#abstracction--hiding the implementation,and showing the user what are important features
'''class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")
        
car1=Car()
car1.start()'''


#encapsulation-- wrapping data and function into single unit



#delete object and onject attributes

'''class Student:
    def __init__(self,name):
        self.name=name

s1=Student("nitish")
print(s1.name)
del s1.name
print(s1.name)'''

#private

class Account:
    def __init__(self,acc_no,acc_passw):
        self.acc_no=acc_no
        self.__acc_passw=acc_passw #by addint two underscores it becomes private it cant be accesed outside of a class

    def __hello(self): #making the method private
        print("hello !")
    def Welcome(self): 
        self.__hello()

acc1=Account("1234","saasasc")
print(acc1.acc_no)
#print(acc1.passw)
#acc1.__hello()
acc1.Welcome()

























