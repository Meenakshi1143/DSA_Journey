
#Question 1: Student Marks Manager

marks = []

for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print(f"Original marks: {marks}")

marks.insert(0, 90)

marks.extend([75, 85])

if 75 in marks:
    marks.remove(75)

removed_mark = marks.pop()

print(f"Removed final mark: {removed_mark}")
print(f"Final marks: {marks}")
print(f"Number of marks: {len(marks)}")



#Question 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print(f"Ascending order: {numbers}")

numbers.reverse()
print(f"Descending order: {numbers}")

num = int(input("Enter a number: "))

if num in numbers:
    print(f"{num} is found in the list")
    print(f"Count: {numbers.count(num)}")
    print(f"First index: {numbers.index(num)}")
else:
    print(f"{num} is not found in the list")

print(f"Smallest value: {min(numbers)}")
print(f"Largest value: {max(numbers)}")
print(f"Total: {sum(numbers)}")


#Question 3: Even and Odd Number Separator
numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

print(f"First three values: {numbers[:3]}")
print(f"Last three values: {numbers[-3:]}")

backup = numbers.copy()

numbers.clear()

print(f"Original list: {numbers}")
print(f"Backup list: {backup}")


#Question 4: Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"] 
n = set(names)
#print(type(n))
n.add("Meera")
n.update(["Arun","Priya"])
if "John" in n:
    n.remove("John")
n.discard("David")
for name in n:
    print(name)


#Question 5: Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
union_ = python_students.union(da_students)
intersection_ = python_students.intersection(da_students)
diff_ = python_students.difference(da_students)
symDiff_ = python_students.symmetric_difference(da_students)
sub_ = da_students.issubset(python_students)
super_ = python_students.issuperset(da_students)
disJoint_ = python_students.isdisjoint(da_students)
print(union_,intersection_, diff_, symDiff_, sub_, super_, disJoint_, sep ="\n")

print("-----Students from both courses-----")
for students in union_ :
    print(students)
print("-----Students learning both courses-----")
for students in intersection_:
    print(students)
print("-----Students learning only Python-----")
for students in diff_ :
    print(students)
print("-----Students learning only one of the courses-----")
for students in symDiff_:
    print(students)

print("\nIs DA a subset of Python: ", sub_)

print("Is Python a superset of DA: ", super_)

print("Are Python and DA disjoint: ", disJoint_)




