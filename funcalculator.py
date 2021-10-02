def add(x,y):ins

"""This function adds 2 numbers"""
    return x+y

def subtract(x,y):

    """This function subtracts 2 numbers"""

    return x-y

def multiply(x,y):

    """This function multiplies 2 numbers"""

    return x*y



#take input from user

print("Select Operation")

print("1.Add")

print("2.Subtract")

print("3.Multiply")

print("4.Divide")

print("5.Power")

choice=input("Enter Choice 1/2/3/4/5:")

num1= int(input("Enter the first number:"))

num2= int(input("Enter the second number:"))


#Printing Output Based On Input

if choice =='1':

    print (num1,"+", num2,"=", add(num1,num2))

elif choice == '2':

    print(num1,"-", num2,"=", subtract(num1,num2))

elif choice == '3':

    print(num1,"x", num2,"=", multiply(num1,num2))

elif choice == '4':

    print(num1,"/", num2,"=", divide(num1,num2))

elif choice == '5':

    print(num1,"^", num2,"=", power(num1,num2))

else:

    print ("Invalid Input")

