from utils.account import Account

class CurrentAccount(Account):
    def __init__(self, initial_balance, account_type):
        super().__init__(initial_balance, account_type)