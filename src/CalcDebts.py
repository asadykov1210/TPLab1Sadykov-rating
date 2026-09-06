# -*- coding: utf-8 -*-
import pytest
from src.CalcDebts import CalcDebts

def test_count_debtors():
    data = {
        "Иванов Иван": [("математика", 80), ("литература", 59)],
        "Петров Петр": [("математика", 100), ("физика", 90)],
        "Сидоров Сидор": [("химия", 60), ("биология", 55)]
    }
    calc = CalcDebts(data)
    assert calc.count_debtors() == 2
