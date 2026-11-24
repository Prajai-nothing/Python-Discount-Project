class DiscountCalculator:

    def calculate_discount(self, customer_type, amount):

        if customer_type == "PREMIUM":
            if amount >= 5000:
                return amount * 0.20
            elif amount >= 2000:
                return amount * 0.15
            else:
                return amount * 0.10

        elif customer_type == "REGULAR":
            if amount >= 5000:
                return amount * 0.10
            elif amount >= 2000:
                return amount * 0.05
            else:
                return 0

        return 0

    def calculate_final_amount(self, customer_type, amount):

        discount = self.calculate_discount(
            customer_type,
            amount
        )

        return amount - discount