from discount import DiscountCalculator

calculator = DiscountCalculator()

def test_premium_customer():

    final_amount = calculator.calculate_final_amount(
        "PREMIUM",
        5000
    )

    assert final_amount == 4000


def test_regular_customer():

    final_amount = calculator.calculate_final_amount(
        "REGULAR",
        5000
    )

    assert final_amount == 4500


def test_no_discount():

    final_amount = calculator.calculate_final_amount(
        "REGULAR",
        1000
    )

    assert final_amount == 1000