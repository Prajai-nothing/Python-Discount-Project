from customer import Customer
from order import Order

customer1 = Customer(
    101,
    "Prajai",
    "PREMIUM"
)

customer1.display_customer()

order1 = Order(
    5001,
    customer1,
    6000
)

order1.generate_bill()
print("Completed")