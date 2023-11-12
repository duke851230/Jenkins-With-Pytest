from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.operator import Operator

from src.operator import (
    AddOperator, MinusOperator, calculate_two_number
)


def test_add_operator_calculate() -> None:
    num1: float = 10.0
    num2: float = 8.0
    add_operator: Operator = AddOperator()

    res: float = add_operator.calculate(num1, num2)
    print(f"res: {res}")

    assert res == num1 + num2


def test_minus_operator_calculate() -> None:
    num1: float = 10.0
    num2: float = 8.0
    minus_operator: Operator = MinusOperator()

    res: float = minus_operator.calculate(num1, num2)
    print(f"res: {res}")

    assert res == num1 - num2


def test_calculate_two_number() -> None:
    num1: float = 10.0
    num2: float = 8.0
    minus_operator: Operator = MinusOperator()

    res: float = calculate_two_number(minus_operator, num1, num2)
    print(f"res: {res}")

    assert res == num1 - num2


def test_random() -> None:
    import random

    random_number: int = random.randint(1, 50)
    print(f"random_number: {random_number}")

    assert random_number % 2 == 0

