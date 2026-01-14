def calculator(a,b,user_choice):
    if (user_choice == '+'):
        return (a+b)
    
    elif(user_choice == '-'):
        return (a-b)
    
    elif(user_choice == '*'):
        return (a*b)
    
    elif(user_choice == '/'):
        return (a/b)
    
    elif(user_choice == '%'):
        return (a%b)
    
    else:
        return 

while(1):
    a=int(input("enter the number a: ")) 
    b=int(input("enter the number b: "))   

    print("1. + ")       
    print("2. - ")       
    print("3. * ")       
    print("4. / ")       
    print("5. % ")     

    user_choice=input("enter your choice: ")

    print(calculator(a,b,user_choice))  