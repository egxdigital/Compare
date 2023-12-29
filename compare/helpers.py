"""Compare Helpers

This module contains the helper function definitions for the Compare program.
"""
from typing import List
from decimal import Decimal, ROUND_HALF_UP
from compare.config import *

def sum_decimal_amounts(amounts: List[Decimal]) -> Decimal:
    """Takes a list of Decimal amounts and returns the unrounded sum as type Decimal.

    Args:
        amounts (List[Decimal]): List of Decimal amounts

    Returns:
        Decimal: Decimal value representing the sum
    """
    return sum(amounts)


def decimal_quantize(amt: str) -> Decimal:
    """Takes a currency amount as a string and returns a Decimal value stored to two decimal places

    Args:
        amt (str): dollar amount

    Returns:
        Decimal: value to two decimal places
    """
    return Decimal(amt).quantize(
        Decimal('0.01'),
        rounding=ROUND_HALF_UP
    )