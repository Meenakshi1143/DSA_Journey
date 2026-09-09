'''
Python Project - POP / OOP - DSA (logic based - pattern based - platforms)
POP (Procedure Oriented Programming) - Dividing the entire code into blocks -- Procedures -- functions (def)
Functions - A reusable block of code (A block of statements which performs a specific task)

Syntax:
def <function_name>(parameters):     #func def
    """Doc String"""
    stmt(s)...
    .............      #body of func
    return values(s)...
function_name(arguments) #fun call

#Simple Scenario to understand

def add(a, b):
    """Addition Function"""
    c = a + b
    #return a +b 
    return c
print(add(45,87))
c, d = "Codegnan", "Institution"
print(add(c, d))

e, f =map(str,input("Enter values: ").split(" "))
print(e, f)
print(add(e, f))
print(add([1,2,3,4], [5,6,7,8]))

#print(add([1,2,3,4])) #Positional arguments fail
#Variable length arguments - *args we can pass any number of positional
#Arguments - Data will be stored in tuple...


def sample(*a):
    print(a)
    print(type(a))
sample()
sample(34,6,7,987,5)
sample("Code", [1, 8, 9], 57)


marks = [86,79,90,76]
sample(marks)
sample(*marks)
a, *b, c = 12, "Mam", "Sir", 654, 890
#a= 12, "Mam", "Sir", 654, 890
#print(a)
print(a, b, c, sep = "\n")


def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        #print(i)
        #if type(i) in [int, float]:
        if type(i) == int or type(i) == float:
            result = result + i
    return result
print(add(2, 3, 4))
print(add(2, 'codegnan', 3, 4))

'''

#Keyword arguments - we can pass the name for the arguments
#def batch(name, age, place):
#def batch(name = "ABCD", age, place): // Error - non default always follows parameter with default argument 

def batch(name, age, place  = 'VJD'):
    """keyword argument usage"""
    print(f'{name} is in {place} from {age} years')
batch('Codegnan', 1,'Vizag')
batch('Codegnan', "hyd")
batch(place = 'Pune', age = 4, name = 'Vandan')


print(4, 46)
print(4, 46, sep = ":")

# Keyword variable length arguments (**kwargs) - any number of Keyword arguments, data is stored in dictionary
def batch(**a):
    """Keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(Name = "Tej", Age = 21, Place = "Vizag", Branch = "CSE")

data = {
    'Name' : ['Pavan', 'Junnu'],
    'Place' : ['USA', 'Singapore']
    }
data.update({'Batch' : 'PFS-VSP-004'})
batch(**data)
    
