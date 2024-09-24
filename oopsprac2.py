# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.


class Account:


    # parameterized contructor
    def __init__(self,balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    
    def print_balance(self):
        print("Amount in the bank", self.balance)
        return self.balance
        
    def debit(self,debit_amount):
        self.balance  = self.balance - debit_amount

    def credit(self,credit_amount):
         self.balance  = self.balance + credit_amount

    
    
    
    
s1 = Account(10000,"5767567565")
print(s1.acc_no)
print(s1.balance)

s1.print_balance()
s1.debit(1000)
s1.print_balance()

s1.credit(7000)
s1.print_balance()