"""Compare Helpers

This module contains the helper function definitions for the Compare program.
"""
from typing import List
from decimal import Decimal, ROUND_HALF_UP
from compare.config import *

def shift_and_scale_transformation(components):
    """Takes a list of components containing a 'score' property and returns
    the same list of components with a new property 'transformed_score'

    Args:
        components List[dict]: List of components containing property 'score'

    Returns:
        List[dict]: List of components containing new property 'transformed_score'
    """
    original_scores = [component['score'] for component in components]
    
    # Shift scores so minimum is 0
    min_score = min(original_scores)
    shifted_scores = [score - min_score for score in original_scores]
    
    # Scale scores to range 0 - 100
    max_score = max(shifted_scores)
    scaled_scores = [score * (100 / max_score) for score in shifted_scores]

    # Create new dictionaries with the transformed scores
    transformed_components = [
        {**component, 'transformed_score': decimal_quantize(transformed_score)}
        for component, transformed_score in zip(components, scaled_scores)
    ]

    return transformed_components

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