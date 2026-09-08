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

'''

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
