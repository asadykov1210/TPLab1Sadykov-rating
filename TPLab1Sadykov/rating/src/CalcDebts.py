# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebts:
    def __init__(self, data: DataType) -> None:
        self.data = data

    def count_debtors(self) -> int:
        count = 0
        for student, subjects in self.data.items():
            if any(score < 61 for _, score in subjects):
                count += 1
        return count
