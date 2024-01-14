"""Test Compare

This module contains the test case for the Compare program.

Usage
    python -m unittest tests.test_compare
"""
import pytest
import argparse
from typing import List
from decimal import Decimal

from compare.config import *
from compare.helpers import *
from compare.compare import Compare
from compare.arg_parser import create_parser
from tests.utils.helpers import get_typical_command_and_payload, get_typical_payload_and_price_comparison_result, get_typical_payload_with_weights_and_score_comparison_result

@pytest.fixture
def compare_parser():
    return create_parser()

def run_command(parser: argparse.ArgumentParser, command: List[str]) -> Compare:
    args = parser.parse_args(command)
    options = vars(args)
    compare = Compare(parser, options)
    return compare

def test_compare_for_payload_size(compare_parser: argparse.ArgumentParser) -> None:
    command, result_payload = get_typical_command_and_payload()
    compare = run_command(compare_parser, command)
    assert len(compare.payload) == 3, "Payload size should be 3"

def test_compare_for_payload_match(compare_parser: argparse.ArgumentParser) -> None:
    command, expected_result = get_typical_command_and_payload()
    compare = run_command(compare_parser, command)
    result = compare.payload
    assert result == expected_result, "Payloads should match"

def test_compare_for_handling_aliases_and_partial_attribute_names(compare_parser: argparse.ArgumentParser) -> None:
    command, result_payload = get_typical_command_and_payload()
    compare = run_command(compare_parser, command)
    for component in compare.payload:
        for attr in component.items():
            attr_name, attr_value = attr
            if attr_name in compare.valid_attribute_types.keys():
                pass
            else:
                for reserved_attr_name in compare.valid_attribute_types.keys():
                    assert not reserved_attr_name.startswith(attr_name), "Partial or alias reserved attribute names should be detected"

def test_compare_for_interpreting_component_attribute_value_types(compare_parser: argparse.ArgumentParser) -> None:
    command, result_payload = get_typical_command_and_payload()
    compare = run_command(compare_parser, command)
    for component in compare.payload:
        for attr in component.items():
            attr_name, attr_value = attr
            if attr_name not in compare.valid_attribute_types.keys():
                assert type(attr_value) == Decimal, f"'{attr_name}' is not on list of reserved attrs and is therefore a part with a price of type 'float'"
            else:
                attr_type = compare.valid_attribute_types.get(attr_name)
                if attr_type == 'float':
                    assert type(attr_value) == float, f"'{attr_name}' should be type float"
                if attr_type == 'string':
                    assert type(attr_value) == str, f"'{attr_name}' should be type str"

def test_class_method_compare_by_price() -> None:
    payload, expected_result = get_typical_payload_and_price_comparison_result()
    result = Compare.compare_by_price(payload)
    assert result == expected_result, "Should return a list of components sorted in ascending order by total_price"

def test_instance_method_run_price_comparison(compare_parser: argparse.ArgumentParser) -> None:
    command, unsorted_result = get_typical_command_and_payload()
    expected_result = sorted(unsorted_result, key=lambda x : x['total_price'])
    compare = run_command(compare_parser, command)
    result = compare.result_payload
    assert result == expected_result, "Should return a list of components sorted in ascending order by price"

def test_class_method_compare_by_score() -> None:
    payload, weights, expected_result = get_typical_payload_with_weights_and_score_comparison_result()
    result = Compare.compare_by_score(payload, weights)
    assert result == expected_result, "Should return a list of components sorted in ascending order by score"
