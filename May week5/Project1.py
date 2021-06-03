"""
Create a python class ATM which has a parametrised constructor (card_no, acc_balance).
Create methods withdraw(amount) which should check if the amount is available on the
account if yes, then deduct the amount and print the message “Amount withdrawn”, if the
amount is not available then print the message “OOPS! Unable to withdraw amount, Low
balance”. Create another method called, deposit, which should deposit amount if amount is
positive and should print message “Amount deposited”. If not, print message “Invalid amount
to deposit”. Create a method called getBalance which should print current balances at any
given point of time.

Example:  atm_acc_1 = ATM(“1234”, 400)
          atm_acc_2 = ATM(“10001”, 100)
"""


class ATM:
    def __init__(self,card_no,acc_balance):
    #initiation of variables
        self.card_no = card_no
        self.acc_balance = acc_balance
    
    def withdraw(self,w_amount):
    #withdraw section
        self.w_amount = w_amount
        
        self.acc_balance -= self.w_amount
        if self.acc_balance > 0 :
            return "Amount withdrawn"
        else:
            self.acc_balance += self.w_amount
            return "OOPS! Unable to withdraw amount, Low balance"
            
        
    def deposit(self,d_amount):
    #deposit section
        self.d_amount = d_amount
        
        if self.d_amount > 0 :
            self.acc_balance += self.d_amount
            return "Amount deposited" 
        else:
            return "Invalid amount to deposit"
        
    def getBalance(self):
    #final section
        return self.acc_balance
        

atm_acc_1 = ATM(123,400)
print(atm_acc_1.withdraw(300)) #Amount withdrawn
print(atm_acc_1.deposit(-100)) #Invalid amount to deposit
print(atm_acc_1.getBalance()) #100
print(atm_acc_1.withdraw(300)) #OOPS! Unable to withdraw amount, Low balance
print(atm_acc_1.getBalance()) #100
