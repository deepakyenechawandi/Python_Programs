def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select the operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

Operation=int(input("Select the operation:"))
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))

if Operation==1:
    print(f"Addition: {num_1} + {num_2} = {add(num_1,num_2)}")

elif Operation==2:
    print(f"Substraction: {num_1} - {num_2} = {sub(num_1,num_2)}")

elif Operation==3:
     print(f"Multiplication: {num_1} * {num_2} = {mul(num_1,num_2)}")

elif Operation==4:
     print(f"Division: {num_1} / {num_2} = {div(num_1,num_2)}")

else:
    print("Invalid input")
    
    
