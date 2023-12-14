class Customer:
    def __init__(self, customer_id, name, email, phone_number, address, credit_score):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._credit_score = credit_score

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def address(self):
        return self._address

    @property
    def credit_score(self):
        return self._credit_score

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @name.setter
    def name(self, name):
        self._name = name

    @email.setter
    def email(self, email):
        self._email = email

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @address.setter
    def address(self, address):
        self._address = address

    @credit_score.setter
    def credit_score(self, credit_score):
        self._credit_score = credit_score
