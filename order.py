from discount import DiscountCalculator

class Order:

    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount

    def generate_bill(self):

        calculator = DiscountCalculator()

        discount = calculator.calculate_discount(
            self.customer.customer_type,
            self.amount
        )

        payable_amount = calculator.calculate_final_amount(
            self.customer.customer_type,
            self.amount
        )

        print("\n-------- BILL --------")
        print("Order ID :", self.order_id)
        print("Customer :", self.customer.name)
        print("Order Amount :", self.amount)
        print("Discount :", discount)
        print("Final Amount :", payable_amount)
        print("----------------------")