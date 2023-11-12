from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.operator import Operator

from src.operator import (
    AddOperator, MinusOperator, calculate_two_number
)


if __name__ == "__main__":
    add_operator: Operator = AddOperator()
    minus_operator: Operator = MinusOperator()

    print(calculate_two_number(add_operator, 10, 5))
    print(calculate_two_number(minus_operator, 10, 5))