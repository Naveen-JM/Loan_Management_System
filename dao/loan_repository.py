from abc import ABC, abstractmethod
from Entity.Loan import Loan

class LoanRepository(ABC):
    @abstractmethod
    def applyLoan(self, loan: Loan):
        pass

    @abstractmethod
    def calculateInterest(self, loan_id):
        pass

    @abstractmethod
    def loanStatus(self, loan_id):
        pass


    @abstractmethod
    def loanRepayment(self, loan_id, amount):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(self, loanId):
        pass
