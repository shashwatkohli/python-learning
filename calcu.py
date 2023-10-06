def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Cannot Divide by 0"
    else:
        return x/y

print("Make Selection")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice= input("Choose Command 1/2/3/4: ")

    if choice in ('1' ,'2' ,'3' ,'4'):
        num1= float(input("Enter First Number Here: "))
        num2= float(input("Enter Second Number Here: "))

        if choice == '1':
            print ("Result: ", add(num1,num2))

        if choice == '2':
            print("Result: ", subtract(num1,num2))

        if choice == '3':
            print ("Result: ", multiply(num1,num2))

        if choice == '4':
            print ("Result: ", divide(num1,num2))
    else:
        print("Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break








