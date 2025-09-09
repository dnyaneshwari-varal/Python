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
      acc_type=input("Enter Account Type: ")
      user_acc[acc_no]={"Account_no":acc_no,"name":name,"Balance":balance,"Acc_type":acc_type}
            
    
      #want to continue
      add_or_not=int(input("do you want to add another account? if yes enter 1 if not enter 0: "))
      if add_or_not==0:
        break
  
  #print(user_acc)

#deposit money
def deposit_money(acc_no,money):
    
    user_acc[acc_no]["Balance"] +=money
    print(user_acc[acc_no])


#withdraw money
def withdraw_money(acc_no,money):
    user_acc[acc_no]["Balance"] -=money
    print(user_acc[acc_no],"{} is withdraw and curreny amount is {}".format(money,user_acc[acc_no]["Balance"]))


#Display data
def display_data():
    for acc_num in user_acc:
        print(user_acc[acc_num])

#Display Balance
def display_balance():
    for acc_num in user_acc:
        print(user_acc[acc_num]["name"],"balance is: ",user_acc[acc_num]["Balance"])





user_acc={}
while True:       
            
    print("1.add new account of users: ")
    print("2.Deposit Money: ")
    print("3.Withdraw money: ")
    print("4.Display Acount details: ")
    print("5.Display Balance: ")
    print("6:exit ")

    
    choice=int(input("Enter choice: "))
    if choice == 1:
        add_account()
    elif choice==2:
        acc_no=int(input("Enter Acc no where you want to deposite: "))
        money=int(input("Enter how many amount you want to deposite"))
        deposit_money(acc_no,money)
    elif choice==3:
        acc_no=int(input("Enter Acc no where you want to withdrow money: "))
        money=int(input("Enter how many amount you want to withdrow"))
        withdraw_money(acc_no,money)
    elif choice==4:
        acc_no=int(input("Enter Acc no where you want to withdrow money: "))
        display_data()
        
    elif choice==5:
        display_balance()

    elif choice==6:
        break

    else:
        print("Enter valid choice")



#2Partition the string based on the first occurrence of a given word using function named partitionstr().


def partitionstr(text,word):
    result=text.partition(word)
    print(result)
        


text=input("Enter text to particition: ")
word=input("Enter the word from you want partition text: ")

partitionstr(text,word)
'''
#3. WAP to generate grades(student_dict) that takes a dictionary containing student names as keys and their marks (out of 100) as values. The program should create a new dictionary where students are assigned grades:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: Below 60

def student_dict(stud_mark):
    stude_grade={}
    for name in stud_mark:
        mark=stud_mark[name]
        if mark>=90 and mark<=100:
            stude_grade[name]="A"

        elif mark>=80 and mark<=89:
            stude_grade[name]="B"
        elif mark>=70 and mark<=79:
            stude_grade[name]="C"
        elif mark>=60 and mark<=69:
            stude_grade[name]="D"
        else:
            stude_grade[name]="F"

    return stude_grade     



stud_mark={}

while True:
    name=input("Enter Student Name: ")
    marks=int(input("marks"))
    stud_mark[name]=marks
    ch=int(input("if you add press 1 if not then press 0: "))
    if ch==0:
        break
   
print(stud_mark)
print(student_dict(stud_mark))



































