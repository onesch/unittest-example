class BankAccount:
    """
    A class representing a bank account.
    """

    def __init__(
            self, account_number: int, account_holder: str, balance: float = 0
            ):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the account.

        :param amount: The amount to be deposited. Must be positive.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to be withdrawn.
            Must be positive and less than or equal to the
            current balance.
        :raises ValueError: If the amount is negative or exceeds the
            current balance.
        """
        if amount < 0 or amount > self.balance:
            raise ValueError("Insufficient funds or amount must be positive.")

        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        :return: The current balance.
        """
        return self.balance

    def transfer(self, amount: float, target_account: "BankAccount"):
        """
        Transfers a specified amount to another bank account.

        :param amount: The amount to be transferred.
            Must be positive and less than or
            equal to the current balance.
        :param target_account: The target bank account to which the
            amount will be transferred.
        :raises ValueError: If the amount is negative or
            exceeds the current balance.
        """
        if amount < 0 or amount > self.balance:
            raise ValueError("Insufficient funds or amount must be positive.")
        self.balance -= amount
        target_account.balance += amount

    def __str__(self) -> str:
        """
        Returns a string representation of the bank account,
        including the account number, holder, and balance.

        :return: A string representing the bank account.
        """
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance}"
        )
