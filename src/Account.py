from dataclasses import dataclass
# Account class
@dataclass
class Account:
    alias: str
    balance: float = 0.0

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError("Account balance cannot be negative.")