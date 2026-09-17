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

'''
#Task: Create a function using *args and **kwargs

def shopping_cart(*items, **details):
    print("Items:")
    for item in items:
        print(item)

    print("\nOrder Details:")
    for key, value in details.items():
        print(key, ":", value)


shopping_cart(
    "Laptop",
    "Mouse",
    "Keyboard",
    customer=input("Enter Customer Name: "),
    city=input("City: " ),
    payment=input("Payment Mode: ")
)




#task
#Creat a function withe usage of *args & **Kwargs with real time secenrio

def student_marks(*args, **kwargs):
    """Here takes student name marks and college and bank detals"""
    for student in args:
        print("Name:", student[0])
        print("Python:", student[1])
        print("SQL:", student[2])
        print("Java:", student[3])
        print()

    print("College:", kwargs["college"])
    print("Branch:", kwargs["branch"])


student_marks(
    ("Lavanya", 85, 90, 80),
    ("Likhitha", 90, 88, 85),
    college="Amrutha College",
    branch="Computer Science"
)



# Task
# Create a function with usage of *args & **kwargs
# Real-time scenario: Shopping Order Management

def shopping_details(*args, **kwargs):
    """Takes product details and customer/order details"""

    for product in args:
        print("Product:", product[0])
        print("Quantity:", product[1])
        print("Price:", product[2])
        print("Category:", product[3])
        print()

    print("Customer:", kwargs["customer"])
    print("Place:", kwargs["place"])
    print("Payment:", kwargs["payment"])


shopping_details(
    ("Laptop", 1, 55000, "Electronics"),
    ("Mouse", 2, 800, "Accessories"),
    ("Keyboard", 1, 1500, "Accessories"),
    customer="Meena",
    place="Vizag",
    payment="UPI"
)


# Task
# Create a function with usage of *args & **kwargs
# Real-time scenario: Shopping Order Management

def shopping_details(*args, **kwargs):
    """Takes product details and customer/order details"""

    for product in args:
        print("Product:", product[0])
        print("Quantity:", product[1])
        print("Price:", product[2])
        print("Category:", product[3])
        print()

    print("Customer:", kwargs["customer"])
    print("Place:", kwargs["place"])
    print("Payment:", kwargs["payment"])


n = int(input("Enter number of products: "))

products = []

for i in range(n):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    category = input("Enter category: ")

    products.append((product, quantity, price, category))


customer = input("Enter customer name: ")
place = input("Enter place: ")
payment = input("Enter payment method: ")

shopping_details(
    *products,
    customer=customer,
    place=place,
    payment=payment
)
