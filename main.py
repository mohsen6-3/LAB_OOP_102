from Lab import BankAccount

person1 = BankAccount("Ahmed", 5000)
# Display initial balance and account holder
print("\nBank Account :")
print('-' * 15)
print("Initial Account Information:")
print(person1.get_account_holder())
print(person1.get_balance())
print()

# Deposit money
print("Deposit:")
print(person1.deposit(2000))
print(person1.get_account_holder())
print(person1.get_balance())
print()

# Withdraw money 
print("Withdraw:")
try:
    print(person1.withdraw(4000))
except ValueError as e:
    print('Error: ' + str(e))
print(person1.get_account_holder())
print(person1.get_balance())
print()
