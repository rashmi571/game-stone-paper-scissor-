class Account:
    def __init__(self):
        self.Account_holder = ""
        self.account_no = 0
        self.amount = 0
        
        
    def getdata(self):
        self.Account_holder=input("Enter your name: ")
        self.account_no=int(input("Enter your account number: "))
        self.amount=int(input("Enter your starting amount: "))
        
    def deposit(self):
        balance = int(input("Enter the deposit amount: "))
        if balance > 0:
            self.amount += balance
            print("Money deposited successfully")
        else:
            print("Invalid amount")

    
    def withdraw(self,balance):
       
        if balance <= self.amount:
            self.amount -= balance
            print("Money withdrawn successfully")
        else:
            print("Insufficient balance")   
            
    def show_detail(self):
        print(f"{self.Account_holder} Account details")
        print(f"Name: {self.Account_holder}")
        print(f"Account number: {self.account_no}")
        print(f"Total Amount: {self.amount}")

#-----------------------SAVING ACCOUNT------------------------------        
class Saving_account(Account):
    def __init__(self,interest=0.2):
        self.minimum_bal=1000
        self.interest=interest
        super().__init__()
        
    def withdraw(self):
        balance=int(input("Enter the amount"))
        if self.amount - balance >= self.minimum_bal:
            super().withdraw(balance)    
        else:
             print("Can't withdraw. Minimum balance must be maintained")   
        
    def calculate_interest(self):
        si=(self.amount * self.interest)/100
        print("Interest earned: ",si)    

#---------------------------CURRENT ACCOUTN------------------------
class Current_account(Account):
    def __init__(self):
        super().__init__()
        self.minimum_bal=5000

    def withdraw(self):
        balance = int(input("Enter withdraw amount: "))
        if self.amount - balance >= self.minimum_bal:
            super().withdraw(balance)
        else:
            print("Minimum balance of 5000 required")

        
        
        
                
        
print("===welcome to our bank===")

print("1. Saving Account \n 2.Current Account")
ch= int(input("Choose Account Type: "))

if ch == 1:
    b=Saving_account()
    b.getdata()
elif ch == 2:
    b=Current_account()
    b.getdata()
else:
    print("Invalid choice, Try another choice")
    exit()        
    

while True:
    print("Choice one")
    print("1.Deposit money \n 2.Withdraw money \n 3.Show deatils \n 4.Exit")     
    choice=int(input("Enter your choice: "))


    if choice == 1:
        b.deposit()
    elif choice == 2:
        b.withdraw()
    elif choice == 3:
        b.show_detail()
    elif choice == 4:
        print("Thanks for visit")
        break
    else:
        print("Invalid choice ,Try another choice")       
                    