'''

Scenario to understand (*args, **kwargs)
Modules - Some interesting cases - Projects (Virtual Assistant, EMail Automation)
OOP - GitHub (Branch)

#Employee Details

def employees(*names, **settings):
    """Employee Details along with their settings"""
    print("Employee Names")
    print("---------")
    for employee in names:
        print("-", employee)
    for key, value in settings.items():
        print(f"{key} - {value}")
#names = input("Enter name: ").split(",")
#employees(*names,
employees("Ramu", "Seetha", "Geetha",
          department = "Operation",
          experience_letter = True,
          salary = True)

Module - It is a simple Python file (resuable, organized code)
import


Organization - class
Employees - function(Methods)
Performance Metrics - functions
Increment - function

Package
   |
Module
import keyword
   |
organization--> Class
   |
Employeees-->Function
Performance Metrics-->Function
Increment-->Function
   |
Emp1,Emp2,Emp3....-->Objects

'''




def employees(*names, **settings):
    """Employee Details along with their settings"""
    print("Employee Names")
    print("---------")
    for employee in names:
        print("-", employee)
    for key, value in settings.items():
        print(f"{key} - {value}")
#names = input("Enter name: ").split(",")
#employees(*names,
'''employees("Ramu", "Seetha", "Geetha",
          department = "Operation",
          experience_letter = True,
          salary = True)'''

details = {
    'Organization' : 'Codegnan',
    'Year' : 2018,
    'Branches' : ['Vijaywada', 'Hyderabad', 'Visakhapatnam']}
#if __name__ == "__main__":
print(__name__) #Dunder methods - Magic methods










