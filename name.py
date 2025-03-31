class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    def _init_(self, message="Insufficient funds in the account."):
        super()._init_(message)

class BankAccount:
    def _init_(self, balance=0):
        """Initialize the bank account with a starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Deposit a certain amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a certain amount from the account, handling insufficient funds."""
        if amount > self.balance:
            raise InsufficientFundsError(f"Withdrawal failed: Requested ${amount:.2f}, Available ${self.balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}. New Balance: ${self.balance:.2f}")
    
    def get_balance(self):
        """Return the current balance."""
        return self.balance

# Example Usage
if __name__ == "_main_":
    account = BankAccount(100)  # Create account with $100
    account.deposit(50)          # Deposit $50
    try:
        account.withdraw(200)     # Attempt to withdraw $200 (should raise an error)
    except InsufficientFundsError as e:
        print(e)
    account.withdraw(30)         # Withdraw $30
    print(f"Final Balance: ${account.get_balance():.2f}")