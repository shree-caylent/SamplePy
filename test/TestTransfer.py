
import src.User as User, src.Account as Account, src.Transfer as Transfer
import unittest
import yaml

# Load test data from YAML file
with open("test_data.yml", "r") as file:
    test_data = yaml.safe_load(file)

# Unit tests
class TestUserAndAccount(unittest.TestCase):
    def test_user_creation(self):
        for data in test_data["valid_users"]:
            user = User(**data)
            self.assertIsInstance(user, User)

        for data in test_data["invalid_users"]:
            with self.assertRaises(ValueError):
                User(**data)

    def test_account_creation(self):
        for data in test_data["valid_accounts"]:
            account = Account(**data)
            self.assertIsInstance(account, Account)

        for data in test_data["invalid_accounts"]:
            with self.assertRaises(ValueError):
                Account(**data)

    def test_transfer_money(self):
        user = User(**test_data["user_for_transfer"])
        Transfer.transfer_money(user, "savings", "checking", 500)
        self.assertEqual(user.accounts[0].balance, 1000)
        self.assertEqual(user.accounts[1].balance, 1500)

        with self.assertRaises(ValueError):
            Transfer.transfer_money(user, "savings", "checking", 2000)

if __name__ == "__main__":
    unittest.main()