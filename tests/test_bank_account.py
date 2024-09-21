import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.class_ = BankAccount(
            account_number=1123901923,
            account_holder="Bob",
            balance=0
        )
        self.target_account = BankAccount(
            account_number=2384726224,
            account_holder="Tom",
            balance=0
        )

    def test_initial_balance(self):
        self.assertEqual(self.class_.balance, 0)

    def test_no_negative_balance(self):
        with self.assertRaises(ValueError):
            self.class_.withdraw(100)

    def test_deposit(self):
        test_cases = [
            (100, 100),
            (200, 300),
            (500, 800),
        ]

        for amount, expected in test_cases:
            with self.subTest(amount=amount, expected=expected):
                self.class_.deposit(amount=amount)
                self.assertEqual(self.class_.balance, expected)

    def test_negative_deposit(self):
        test_cases = [
            (-1, ValueError),
            (-230, ValueError),
            (-1000, ValueError),
        ]

        for amount, exception in test_cases:
            with self.subTest(amount=amount, exception=exception):
                with self.assertRaises(exception):
                    self.class_.deposit(amount=amount)

    def test_withdraw(self):
        test_cases = [
            (500, 300, 200),
            (1000, 400, 600),
            (200, 200, 0),
        ]

        for deposit_amount, withdraw_amount, expected in test_cases:
            with self.subTest(
                deposit_amount=deposit_amount,
                withdraw_amount=withdraw_amount
            ):
                self.class_.deposit(amount=deposit_amount)
                self.class_.withdraw(amount=withdraw_amount)
                self.assertEqual(self.class_.balance, expected)
                self.class_.balance = 0

    def test_negative_withdraw(self):
        test_cases = [
            (0, -100, ValueError),
            (100, 1000, ValueError),
        ]

        for deposit_amount, withdraw_amount, exception in test_cases:
            with self.subTest(
                deposit_amount=deposit_amount,
                withdraw_amount=withdraw_amount
            ):
                with self.assertRaises(exception):
                    self.class_.deposit(amount=deposit_amount)
                    self.class_.withdraw(amount=withdraw_amount)

    def test_get_balance(self):
        test_cases = [
            (100, 50, 50),
            (200, 50, 150),
        ]

        for deposit_amount, withdraw_amount, expected in test_cases:
            with self.subTest(
                deposit_amount=deposit_amount,
                withdraw_amount=withdraw_amount
            ):
                self.class_.deposit(amount=deposit_amount)
                self.class_.withdraw(amount=withdraw_amount)
                self.assertEqual(self.class_.get_balance(), expected)
                self.class_.balance = 0

    def test_transfer(self):
        test_cases = [
            (1000, 100, 900, 100),
        ]

        for (
            deposit_amount,
            transfer_amount,
            self_balance,
            target_balance
        ) in test_cases:
            with self.subTest(
                deposit_amount=deposit_amount,
                transfer_amount=transfer_amount,
                self_balance=self_balance,
                target_balance=target_balance
            ):
                self.class_.deposit(amount=deposit_amount)
                self.class_.transfer(
                    amount=transfer_amount,
                    target_account=self.target_account
                )
                self.assertEqual(self.class_.balance, self_balance)
                self.assertEqual(self.target_account.balance, target_balance)

    def test_negative_transfer(self):
        test_cases = [
            (1000, 1100, ValueError),
            (1000, -1100, ValueError),
        ]

        for deposit_amount, transfer_amount, exception in test_cases:
            with self.subTest(
                deposit_amount=deposit_amount,
                transfer_amount=transfer_amount
            ):
                with self.assertRaises(exception):
                    self.class_.deposit(amount=deposit_amount)
                    self.class_.transfer(
                        amount=transfer_amount,
                        target_account=self.target_account
                    )

    def test__str__(self):
        expected = (
            "Account Number: 1123901923\n"
            "Account Holder: Bob\n"
            "Balance: 0"
        )
        self.assertEqual(str(self.class_), expected)
