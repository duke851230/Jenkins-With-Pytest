from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def calculate(self, num1: float, num2: float) -> float:
        pass

class AddOperator(Operator):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 + num2

class MinusOperator(Operator):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 - num2


def calculate_two_number(operator: Operator, num1: float, num2: float) -> float:
    res: float = operator.calculate(num1, num2)
    return res