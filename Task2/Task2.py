num1=int(input("Enter First Number :- "))
num2=int(input("Enter Second Number :- "))

option=int(input('''
 Enter 1 For Addition
 Enter 2 For Subtraction
 Enter 3 For Multiplication
 Enter 4 For Division
 Enter 5 For Modules
 Enter 6 For Maximum
 Enter 7 For Minimum
 Enter 8 Fir Equaltiy
                '''))

if option == 1:
    answer=num1 + num2
    print("Addition is ",answer)
    
elif option == 2:
    print("Subtraction is ",num1 - num2)
    
elif option == 3:
    print("Multiplication is ",num1 * num2)
    
elif option == 4:
    print("Division is ",num1 / num2)
    
elif option == 5:
    print("Modules is ",num1 % num2)
    
elif option == 6:
    if num1 > num2:
        print("Num1 is Maximum",num1)
    elif num2 > num1:
        print("Num2 is Maximum",num2)
    else:
        print("Both are same")

elif option == 7:
    if num1 < num2:
        print("Num1 is Minimum")
    elif num2 < num1:
        print("Num2 is Minimum")
    else:
        print("Both Are Same")
elif option == 8:
    if num1 == num2:
        print("NUm1 And Num2 Are Equal")
    else:
        print("Both Are NOt Equal`")
else:
    print("Invalid Nubmer")