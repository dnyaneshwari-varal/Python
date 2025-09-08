'''
#1
#menudriven with functions
#1st is to add an account where we create a nested dictonary of users
#2nd deposit money
#3rd withdraw money
#4th display account details
#5th display balance
#6th exit


def add_account():
  while True:
    
      name=input("Enter name: ")
      acc_no=int(input("Enter Account number: "))
      balance=int(input("Enter balace: "))
      user_acc[acc_no]={"name":name,"Balance":balance}
            
    
      #want to continue
      add_or_not=int(input("do you want to add another account? if yes enter 1 if not enter 0: "))
      if add_or_not==0:
        break
  
  print(user_acc)
def deposit_money():
    for balance in user_acc[acc_no]:
      print(balance)
   

            
print("1.add new account of users: ")
print("2.Deposit Money: ")
print("3.Withdraw money: ")
print("4.Display Acount details: ")
print("5.Display Balance: ")
print("6:exit ")

user_acc={}
choice=int(input("Enter choice: "))
if choice == 1:
    add_account()
elif choice==2:
    dep_acc=int(input("Enter Acc no where you want to deposite: "))
    
    deposit_money(acc_no)




'''
