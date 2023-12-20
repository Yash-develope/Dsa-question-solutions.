def Addition():
        num1=int(input("Enter the Number :"))
        num2=int(input("Enter Second Number :"))
        num3=num1+num2
        print(f"The sum of {num1} and {num2} is {num3}.")
def Substraction():
        num1=int(input("Enter the Number :"))
        num2=int(input("Enter Second Number :"))
        num3=num1-num2
        print(f"The substraction of {num1} and {num2} is {num3}.")
def Multiplication():
        num1=int(input("Enter the Number :"))
        num2=int(input("Enter Second Number :"))
        num3=num1*num2
        print(f"The multiplication of {num1} and {num2} is {num3}.")
def Division():
        num1=int(input("Enter the Number :"))
        num2=int(input("Enter Second Number :"))
        num3=num1/num2
        print(f"The division of {num1} and {num2} is {num3}.")
def Square():
        num1=int(input("Enter the Number :"))
        num2=num1**2
        print(f"The Square of {num1} is {num2}.")
def Cube():
        num1=int(input("Enter the Number :"))
        num2=num1**3
        print(f"The Cube of {num1} is {num2}.")
def average():
    num_input=int(input("Enter the number of the values you want to average :"))
    values=[]
    for i in range(num_input):
        value=int(input(f"Enter the Value {i+1}:"))
        values.append(value)

    average=sum(values)/len(values)
    print(f"The Average of {values} is {average}.")
        
    
print('''Your Choises are :-
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Square
6. Cube
7. average
'''  )            
operation=input("Select the operation :")
if operation=="Addition":
    Addition()
if operation=="Substraction":
    Substraction()
if operation=="Multiplication":
    Multiplication()
if operation=="Division":
    Division()
if operation=="Square":
    Square()
if operation=="Cube":
    Cube()
if operation=="Square":
    Square()
if operation=="average":
    average() 
                     
                     
        
