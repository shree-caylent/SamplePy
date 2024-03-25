import src.Account as Account
import re
import yaml
from dataclasses import dataclass

# Load test data from YAML file
with open("test_data.yml", "r") as file:
    test_data = yaml.safe_load(file)

# Regular expression pattern for email validation
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# User class
@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    accounts: list

    def __post_init__(self):
        # Validate first and last names
        if not all(name.isalpha() for name in [self.first_name, self.last_name]):
            raise ValueError("Names must contain only alphabetic characters.")

        # Validate email
        if not re.match(email_pattern, self.email):
            raise ValueError("Invalid email address.")

        # Initialize accounts
        self.accounts = [Account(alias=alias, balance=balance) for alias, balance in self.accounts]