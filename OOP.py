## EXAMPLE1:

class University():
    name="Mumbai University"
    state="Maharashtra"
    
stud1=University()
print(University.name)
print(University.state)
print("Name=",stud1.name,"State=",stud1.state)


## CONSTRUCTORS:a func defined inside a class which is called as soon as an object of that class is created [ __init__():] a class cannot have multiple constructors

## Self:first parameter of any function defined inside a class; refers to the current object of the class


class University():
    def __init__(self,name,id_no,branch):
        
        self.name=name
        self.id_no=id_no
        self.branch=branch

stud1=University("Sam", "01","IT")
stud2=University("Ram","02", "COMP")

print(stud1.name, stud1.id_no, stud1.branch)
print(stud2.name,stud2.id_no, stud2.branch)


## EXAMPLE 2: create a class circle and compute its area

class Circle():
    pi=3.14
    
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
        
    def area(self):
        self.area = Circle.pi * c1.radius * c1.radius
        return self.area

c1=Circle(5,"Red")
print("The area of the circle is:",c1.area())
print("The color of the circle is:", c1.color)


## EXAMPLE 3: create a class employee and calculate the salary after hike

class Employee():
    hike = 0.5
    
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
        
    def total_salary (self):
        self.total_salary = (Employee.hike + self.salary) * self.salary
        return self.total_salary

emp1=Employee("Ram","HR", 2500)
print("The salary after hike is:",emp1.total_salary())


## get the total count of the employees

class Company():
    count=0
    
    def __init__(self):
        self.status ="Active"
        Company.count+=1
        
    def change_status(self,new_status):
        if self.status in ["Inactive", "Suspended", "Terminated"] and new_status=="Active":
            Company.count+=1
        elif self.status=="Active" and new_status in ["Inactive", "Suspended", "Terminated"]:
            Company.count+=1
        self.status = new_status
        
emp1=Company()
emp2=Company()
emp1.change_status("Suspended")
emp1.change_status("Active")
print("The total count is:",Company.count)
