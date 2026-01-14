try:
    a=int(input("enter the number: "))
    b=int(input("enter the number b: "))
    result=a/b
    print("divided -> ",result) 
except ZeroDivisionError:
    print("Error: cannot divided by zero")
    
except ValueError:   
    print("Error: take valid integer")
    
except Exception as e:
    print("Unexpected error: ",e)     

          
    