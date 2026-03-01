class BankAccount:
    def __init__(self,account_holder:str, initial_balance:float=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount:float): 
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw(self, amount:float): 
            if amount > self.balance:
                raise ValueError(f"Insufficient funds. Current balance: ${self.balance}")
            
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            
            self.balance -=  amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"
     
    def get_account_holder(self):
        return f"Account holder: {self.account_holder}"