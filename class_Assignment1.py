'''
Python Assignment
1. Create a BankAccount class with instance variables account_number and balance.
2. Define a constructor to initialize these variables.
3. Create methods to deposit and withdraw money.
4. Use class variables to track the total number of accounts created.
'''

class BankAccount:
    acc_count=0
    account_number=None
    balance=None

    def __init__(self,acc_num,balance):
        BankAccount.acc_count +=1
        print("Account created: ",BankAccount.acc_count)
        self.account_number=acc_num
        self.balance=balance

    def deposit(self,dep_money):
        print("Current balance is:",self.balance)
        self.balance=self.balance+dep_money
        print("deposite amount is: {}, and total balance in acc is {}".format(dep_money,self.balance))
        
    def withdraw(self,withd_money):
        self.balance=self.balance-withd_money
        print("withdraw amount: {}, Total balance: {}".format(withd_money,self.balance))
        



obj1=BankAccount(100,40000)
obj1.deposit(5000)
obj1.withdraw(2000)

obj2=BankAccount(101,50000)
obj2.deposit(5000)
obj2.withdraw(2000)

obj3=BankAccount(102,70000)
obj3.deposit(5000)
obj3.withdraw(2000)
print("Total number of account created: ",BankAccount.acc_count)



'''
output:


Account created:  1
Current balance is: 40000
deposite amount is: 5000, and total balance in acc is 45000
withdraw amount: 2000, Total balance: 43000
Account created:  2
Current balance is: 50000
deposite amount is: 5000, and total balance in acc is 55000
withdraw amount: 2000, Total balance: 53000
Account created:  3
Current balance is: 70000
deposite amount is: 5000, and total balance in acc is 75000
withdraw amount: 2000, Total balance: 73000
Total number of account created:  3

'''
