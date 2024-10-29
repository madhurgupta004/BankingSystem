class AccountNotFoundException(Exception):
    """Exception raised when account is not found with given account id."""

    def __init__(self, message="No account with matching id"):
        self.message = message
        super().__init__(self.message)



class LowBalanceException(Exception):
    def __init__(self, message="Insufficient balance"):
        self.message = message
        super().__init__(self.message)