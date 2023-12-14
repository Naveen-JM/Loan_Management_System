from Entity.Loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, property_address, property_value, loan_status):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", loan_status)
        self._property_address = property_address
        self._property_value = property_value

    @property
    def property_address(self):
        return self._property_address

    @property
    def property_value(self):
        return self._property_value

    @property_address.setter
    def property_address(self, property_address):
        self._property_address = property_address

    @property_value.setter
    def property_value(self, property_value):
        self._property_value = property_value
