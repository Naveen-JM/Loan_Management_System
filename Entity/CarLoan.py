from Entity.Loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, car_model, car_value, loan_status):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", loan_status)
        self._car_model = car_model
        self._car_value = car_value

    @property
    def car_model(self):
        return self._car_model

    @property
    def car_value(self):
        return self._car_value

    @car_model.setter
    def car_model(self, car_model):
        self._car_model = car_model

    @car_value.setter
    def car_value(self, car_value):
        self._car_value = car_value

