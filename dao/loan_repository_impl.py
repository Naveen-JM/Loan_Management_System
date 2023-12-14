from dao.loan_repository import LoanRepository
from Entity.Loan import Loan
from Exception.invalid_loan_exception import InvalidLoanException
from util.DButil import DBUtil

class LoanRepositoryImpl(LoanRepository):
    def applyLoan(self, loan: Loan):
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            insert_query = "INSERT INTO loans (loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (loan.loan_id, loan.customer.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term, loan.loan_type, loan.loan_status))
            connection.commit()
        except Exception as e:
            print('f The Application failed {e}')
        finally:
            cursor.close()
            connection.close()

    def calculateInterest(self, loan_id):
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            select_query="SELECT principal_amount,interest_rate,loan_term FROM Loan WHERE loan_id=%S"
            cursor.execute(select_query,(loan_id))
            loan_info=cursor.fetchone()

            if not loan_info:
                raise InvalidLoanException("LOAN is INVALID")

            principal_amount,interest_rate,loan_term=loan_info

            interest=(principal_amount*interest_rate*loan_term)/12
            return interest
        except Exception as e:
            raise InvalidLoanException("The Interest was not Found:{e}")
        finally:
            cursor.close()
            connection.close()

    def loanStatus(self, loan_id):
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            select_query="SELECT c.credit_score,l.loan_id FROM loan l join customer c ON c.loan_id=l.loan_id"
            cursor.execute(select_query,loan_id)
            credit_score=cursor.fetchone()

            if credit_score is None:
                raise InvalidLoanException("Credit Score is invalid")
            if credit_score > 650:
                loan_status = "Approved"
            else:
                loan_status = "Rejected"

            update_query="UPDATE loan SET loan_status where loan_id=%s"
            cursor.excute(update_query(loan_status,loan_id))
            connection.commit()
        except Exception as e:
            raise InvalidLoanException("loan status was not updated:{e}")
        finally:
            cursor.close()
            connection.close()

    def getAllLoan(self):
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            select_query="SELECT * FROM loan"
            cursor.execute(select_query)
            all_loans=cursor.fetchone()

            if all_loans is None:
                raise InvalidLoanException("loan not found")
            loans = []
            for record in all_loans:
                loan = Loan(*record)
                loan.append(loan)
        except Exception as e:
            raise InvalidLoanException("Loan not found:{e}")
        finally:
            cursor.close()
            connection.close()

    def getLoanById(self, loanId):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()
            select_query = "SELECT * FROM loan where loan_id=%S"
            cursor.execute(select_query)
            all_loans = cursor.fetchone()

            if all_loans is None:
                raise InvalidLoanException("loan not found")
            loans = []
            for record in all_loans:
                loan = Loan(*record)
                loan.append(loan)
        except Exception as e:
            raise InvalidLoanException("Loan not found:{e}")
        finally:
            cursor.close()
            connection.close()

    def loanRepayment(self, loanId, amount):
        try:
            # Example: Connect to the database and retrieve loan details
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Replace with your actual SQL select statement to retrieve loan details
            select_query = "SELECT principal_amount, interest_rate, loan_term, emi_count FROM loans WHERE loan_id = %s"
            cursor.execute(select_query, (loanId,))
            loan_details = cursor.fetchone()

            if not loan_details:
                raise InvalidLoanException("Invalid loan. Loan not found.")

            principal_amount, interest_rate, loan_term, emi_count = loan_details

            # Calculate EMI using the formula (same as in the previous example)
            monthly_interest_rate = interest_rate / 12 / 100
            emi = (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / \
                      (((1 + monthly_interest_rate) ** loan_term) - 1)

            # Calculate the number of EMIs that can be paid from the given amount
            no_of_emis_paid = int(amount / emi)

            if no_of_emis_paid < 1:
                raise InvalidLoanException("Payment amount is less than a single EMI. Payment rejected.")

                # Update the loan variables based on the payment
            new_emi_count = emi_count + no_of_emis_paid

            # Update the database with the new EMI count
            update_query = "UPDATE loans SET emi_count = %s WHERE loan_id = %s"
            cursor.execute(update_query, (new_emi_count, loanId))
            connection.commit()

            print(f"Payment successful. {no_of_emis_paid} EMIs paid.")
        except Exception as e:
            raise InvalidLoanException(f"Error processing loan repayment: {e}")
        finally:
            cursor.close()
            connection.close()


