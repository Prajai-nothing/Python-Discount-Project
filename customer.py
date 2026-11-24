class Customer:

    def __init__(self, customer_id, name, customer_type):
        self.customer_id = customer_id
        self.name = name
        self.customer_type = customer_type

    def display_customer(self):
        print("Customer ID :", self.customer_id)
        print("Customer Name :", self.name)
        print("Customer Type :", self.customer_type)