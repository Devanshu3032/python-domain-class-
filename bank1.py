class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0.0):
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")
        self.balance = initial_balance
        self.last_withdrawal = None

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        self.last_withdrawal = amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def get_last_withdrawal(self):
        return self.last_withdrawal

def main():
    
    account = BankAccount(1000.0)
    
    while True:
        print("\nBank Account Management System")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Check Last Withdrawal")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                print(f"Current Balance: ${account.check_balance():.2f}")
                
            elif choice == 2:
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    new_balance = account.withdraw(amount)
                    print(f"Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}")
                except (InvalidAmountError, InsufficientFundsError) as e:
                    print(f"Transaction failed: {e}")
                    
            elif choice == 3:
                try:
                    amount = float(input("Enter deposit amount: $"))
                    new_balance = account.deposit(amount)
                    print(f"Deposited ${amount:.2f}. New balance: ${new_balance:.2f}")
                except InvalidAmountError as e:
                    print(f"Transaction failed: {e}")
                    
            elif choice == 4:
                last_withdrawal = account.get_last_withdrawal()
                if last_withdrawal:
                    print(f"Last withdrawal amount: ${last_withdrawal:.2f}")
                else:
                    print("No withdrawals made yet")
                    
            elif choice == 5:
                print("Thank you for using our banking services!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
if __name__ == "__main__":
    main()