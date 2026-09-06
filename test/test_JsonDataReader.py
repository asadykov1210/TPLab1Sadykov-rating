# -*- coding: utf-8 -*-
import json
import tempfile
import os

from src.JsonDataReader import JsonDataReader


def test_json_data_reader_simple():
    data = {
        "Иванов Иван": {
            "математика": 80,
            "литература": 59
        }
    }

    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8"
    ) as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    reader = JsonDataReader()
    result = reader.read(tmp_path)

    os.remove(tmp_path)

    assert "Иванов Иван" in result
    assert ("математика", 80) in result[
        "Иванов Иван"
    ]
    assert ("литература", 59) in result[
        "Иванов Иван"
    ]


def test_json_data_reader_multiple_students():
    data = {
        "Петров Пётр": {"физика": 70},
        "Сидоров Сидор": {"химия": 90}
    }

    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8"
    ) as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    reader = JsonDataReader()
    result = reader.read(tmp_path)

    os.remove(tmp_path)

    assert ("физика", 70) in result[
        "Петров Пётр"
    ]
    assert ("химия", 90) in result[
        "Сидоров Сидор"
    ]
