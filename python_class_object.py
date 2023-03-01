# How to create a class in python

#constructer of class
class Employee:
    def __init__(self,name,salary):
        self.emp_name=name
        self.emp_salary=salary

# methode of a class
    def displayEmployee(self):
        print("Employee name : ",self.emp_name,"Employee salary: ",self.emp_salary)    
        
empl1= Employee ('pawan',1000)
empl2= Employee ('rahul',9202)
empl1.displayEmployee()
empl2.displayEmployee()

