# -*- coding: utf-8 -*-
import pytest

from src.CalcDebts import CalcDebts
from src.Types import DataType


class TestCalcDebts:

    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Иванов Иван": [
                ("математика", 80),
                ("литература", 59)   # должник
            ],
            "Петров Петр": [
                ("математика", 100),
                ("физика", 90)
            ],
            "Сидоров Сидор": [
                ("химия", 60),       # должник
                ("биология", 55)     # должник
            ]
        }

    def test_count_debtors(self, input_data) -> None:
        calc = CalcDebts(input_data)
        assert calc.count_debtors() == 2
