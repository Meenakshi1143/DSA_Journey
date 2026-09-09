'''
#BMI = (weight) / (height)
numberOfTimesUserInput = int(input("Enter a value: ))
for i in range(numberOfTimesUserInput):
    name = input("Enter Name: ")
    weight =  float(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in metres: "))
    if weight > 0 and height > 0:
        bmi = (weight) / ((height)**2)
        print(bmi)
        if bmi < 18.5:
            print(f"Under Weight")
        elif 18.5<= bmi <= 24.9:
            print(f"Normal Weight")
        elif 25<=bmi<= 29.9:
            print(f"Over Weight")
        elif bmi>=30:
            print("Obesity")
    else:
        print(f"Make sure to enter positive values")


#Task - To store the result of name, height, weight, BMI value into a collection



while True:
    try:
        name = input("Enter Name: ")
        weight =  float(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in metres: "))
    
        if weight >=  0 and height >= 0:
            bmi = (weight) / ((height)**2)
            break
        #else:
            #print(f"Make sure to enter positive values")
    except Exception as e:
        print(f"The Error is {e}")

#bmi = (weight) / ((height)**2)
print(bmi)
if bmi < 18.5:
    print(f"Under Weight")
elif 18.5<= bmi <= 24.9:
    print(f"Normal Weight")
elif 25<=bmi<= 29.9:
    print(f"Over Weight")
elif bmi>=30:
    print("Obesity")





numberOfTimesUserInput = int(input("Enter a value: "))

result = []

for i in range(numberOfTimesUserInput):

    name = input("Enter Name: ")
    weight = float(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in metres: "))

    if weight > 0 and height > 0:

        bmi = weight / (height ** 2)

        data = [name, height, weight, bmi]

        result.append(data)

    else:
        print("Make sure to enter positive values")

print(result)




'''



results = []
number_of_users = int(input("Enter the number of users: "))
for i in range(number_of_users):
    while True:
        try:
            name = input("Enter your name: ")
            weight = float(input("Enter the weight in Kgs: "))
            height = float(input("Enter the height in meters: "))

            if weight > 0 and height > 0:
                break
            else:
                print("Enter only positive values")

        except ValueError:
            print("Enter only numeric values for weight and height")

    bmi = weight / (height ** 2)

    if bmi<18.5:
        print(f'{name} is into Under Weight category and BMI is {bmi}')
    elif  18.5<=bmi<=24.9:
        print(f'{name} is into Normal Weight category and BMI is {bmi}')
    elif 25<=bmi<=29.9:
        print(f'{name} is into Over Weight category and BMI is {bmi}')
    elif bmi>=30:
        print(f'{name} is into Obesity category and BMI is {bmi}')

    result = {
        "name": name,
        "weight": weight,
        "height": height,
        "BMI": bmi,
    }

    results.update(result)

print("\nBMI Results:")

for result in results:
    print(result)
