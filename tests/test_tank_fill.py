"""
EGN 321 — Module 1
Tests for the tank fill calculation.

Your final submission must include:
- at least 2 known-correct workbook cases
- at least 1 defect-related regression case
- at least 2 invalid-input cases
"""

import pytest

from src.tank_fill import calculate_tank_volume


def test_known_correct_workbook_case_1():
    # TODO:
    # 1. Choose a workbook row you independently confirmed is correct.
    # 2. Enter its input values.
    # 3. Enter the expected result.
    # 4. Use pytest.approx() for floating-point comparison.
    pytest.skip("Complete this test with a verified workbook case.")


def test_known_correct_workbook_case_2():
    pytest.skip("Complete this test with a second verified workbook case.")


def test_defect_regression_case():
    # TODO:
    # Create a test that proves one Assignment 1.1 defect cannot silently return.
    pytest.skip("Create a regression test based on a defect you found.")


def test_invalid_input_case_1():
    # Example pattern:
    #
    # with pytest.raises(ValueError):
    #     calculate_tank_volume(...)
    pytest.skip("Add an invalid-input test.")


def test_invalid_input_case_2():
    pytest.skip("Add a second invalid-input test.")
