"""Compare Helpers

This module contains the helper function definitions for the Compare program.
"""
from decimal import Decimal, ROUND_HALF_UP
from compare.config import *

def decimal_quantize(amt: str) -> Decimal:
    return Decimal(amt).quantize(
        Decimal('0.01'),
        rounding=ROUND_HALF_UP
    )