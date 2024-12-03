class BankAccount:
    def __init__(self, iban, owner, balance):
        self.iban = iban
        self.owner = owner
        self.balance = balance
        
    def deposit(self,money):
        if money >=0:
            self.balance += money
            print(f"A deposit of {money} dollars has been made")
        else:
            print("Not a valid amount of deposit")
    def take_out(self,money):
        if money>self.balance:
            print(f"Not enough money in balance to take out {money} dollars")
        elif money <= self.balance:
            self.balance -= money
            print(f"Succesfully taken out {money} dollars out of the balance")
        else:
            print("Not a valid amount to take out")
            
    def display_balance(self):
        print(f"The balance currently is: {self.balance}")

iban, owner, balance = 'bgn123456784', "Danail", 0
bank_info_obj = BankAccount(iban, owner, balance)


while True:
    print("Choose what do to: 1. Deposit; 2. Take Out; 3. Display Balance; 4. Exit")
    choice = int(input())
    if choice == 1:
        money = int(input("Write an amount of money: "))
        bank_info_obj.deposit(money)
    elif choice == 2:
        money = int(input("Write an amount of money: "))
        bank_info_obj.take_out(money)
    elif choice == 3:
        bank_info_obj.display_balance()
    elif choice == 4:
       print("Exiting the program")
       break
    else:
       print("Not a valid choice. Choose between 1-4") 