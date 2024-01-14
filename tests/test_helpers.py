import random
from decimal import Decimal, Context, Inexact
from compare.helpers import decimal_quantize, sum_decimal_amounts, shift_and_scale_transformation

def test_shift_and_scale_transformation():
    scores = [
        {'name': 'component1', 'score': -25.62},
        {'name': 'component2', 'score': -90.14},
        {'name': 'component3', 'score': -92.34},
    ]
    expected_result = [
        {**score, 'transformed_score': expected_score}
        for score, expected_score in zip(scores, [Decimal('100.00'), Decimal('3.30'), Decimal('0.00')])
    ]
    result = shift_and_scale_transformation(scores)
    assert result == expected_result, "Transformed scores should range from 0 - 100" 

def test_decimal_quantize_for_two_decimal_places():
    prices = [
        Decimal(f'{random.uniform(0,50)}'),
        Decimal(f'{random.uniform(0,50)}'),
        Decimal(f'{random.uniform(0,50)}'),
    ]
    subtotal = sum(prices)
    print("Before quantize(): ", subtotal)
    total = decimal_quantize(subtotal)
    print("After quantize(): ", total)
    assert total.quantize(Decimal('0.01'), context=Context(traps=[Inexact])), "Should only have two decimal places"

def test_sum_decimal_amounts_for_accurate_money_arithmetic():
    typical_prices_input = [
        '43.20',
        '54.20',
        '10.09',
        '8',
        '3.00'
    ]
    decimal_values = [Decimal(_) for _ in typical_prices_input]
    expected_result = decimal_values[0] + decimal_values[1] + decimal_values[2] + decimal_values[3] + decimal_values[4]
    result = sum_decimal_amounts(decimal_values)
    print("Result:", result, "Expected Result:", expected_result)
    assert result == expected_result

if __name__ == '__main__':
    #test_decimal_quantize_for_two_decimal_places()
    test_sum_decimal_amounts_for_accurate_money_arithmetic()