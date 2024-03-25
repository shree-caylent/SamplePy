# Transfer class
class Transfer:
    @staticmethod
    def transfer_money(user, from_account, to_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        from_account = next((account for account in user.accounts if account.alias == from_account), None)
        to_account = next((account for account in user.accounts if account.alias == to_account), None)

        if from_account is None or to_account is None:
            raise ValueError("Invalid account alias.")

        if from_account.balance < amount:
            raise ValueError("Insufficient balance in the source account.")

        from_account.balance -= amount
        to_account.balance += amount