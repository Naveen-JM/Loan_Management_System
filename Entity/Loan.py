class Loan:
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status):
        self._loan_id = loan_id
        self._customer = customer
        self._principal_amount = principal_amount
        self._interest_rate = interest_rate
        self._loan_term = loan_term
        self._loan_type = loan_type
        self._loan_status = loan_status

    @property
    def loan_id(self):
        return self._loan_id

    @property
    def customer(self):
        return self._customer

    @property
    def principal_amount(self):
        return self._principal_amount

    @property
    def interest_rate(self):
        return self._interest_rate

    @property
    def loan_term(self):
        return self._loan_term

    @property
    def loan_type(self):
        return self._loan_type

    @property
    def loan_status(self):
        return self._loan_status

    @loan_id.setter
    def loan_id(self, loan_id):
        self._loan_id = loan_id

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @principal_amount.setter
    def principal_amount(self, principal_amount):
        self._principal_amount = principal_amount

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self._interest_rate = interest_rate

    @loan_term.setter
    def loan_term(self, loan_term):
        self._loan_term = loan_term

    @loan_type.setter
    def loan_type(self, loan_type):
        self._loan_type = loan_type

    @loan_status.setter
    def loan_status(self, loan_status):
        self._loan_status = loan_status
