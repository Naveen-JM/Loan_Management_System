class InvalidLoanException(Exception):
    def __init__(self, message="Invalid loan. Loan not found."):
        self.message = message
        super().__init__(self.message)
