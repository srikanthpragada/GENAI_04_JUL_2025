# Create an account class with acno, customername, balance
# provide methods to deposit, withdraw, and getbalance
# provide provision for minbalance, which is same for all accounts

class Account:
    """
    Account class represents a bank account with basic operations.
    Attributes:
        min_balance (int): Class variable specifying the minimum balance required.
    Methods:
        __init__(acno, customername, balance=0):
            Initializes an Account instance with account number, customer name, and optional balance.
        deposit(amount):
            Deposits a positive amount into the account.
            Returns True if successful, False otherwise.
        withdraw(amount):
            Withdraws a positive amount from the account if it does not violate the minimum balance.
            Raises ValueError if amount is non-positive or insufficient funds.
        get_balance():
            Returns the current account balance.
    """
    min_balance = 1000  # Class variable for minimum balance

    def __init__(self, acno, customername, balance=0):
        """
        Initializes a new Account instance.

        Parameters:
            acno (int or str): The account number.
            customername (str): The name of the account holder.
            balance (float, optional): The initial account balance. Defaults to 0.
        """
        self.acno = acno
        self.customername = customername
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account balance if sufficient funds are available and the minimum balance is maintained.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Raises:
            ValueError: If the withdrawal amount is not positive.
            ValueError: If the withdrawal would cause the balance to fall below the minimum required.

        Returns:
            bool: True if the withdrawal was successful.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if (self.balance - amount) < Account.min_balance:
            raise ValueError("Insufficient funds to maintain minimum balance")
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


# create an account object and test the methods
if __name__ == "__main__":  
    acc = Account("12345", "John Doe", 5000)
    print(f"Account Number: {acc.acno}, Customer Name: {acc.customername}, Balance: {acc.get_balance()}")
    
    acc.deposit(2000)
    print(f"Balance after deposit: {acc.get_balance()}")
    
    try:
        acc.withdraw(4000)
        print(f"Balance after withdrawal: {acc.get_balance()}")
    except ValueError as e:
        print(e)
    
    try:
        acc.withdraw(3000)  # This should raise an error due to min balance
    except ValueError as e:
        print(e)

