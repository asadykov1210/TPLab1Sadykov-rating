# -*- coding: utf-8 -*-
import json
import pytest

from src.JsonDataReader import JsonDataReader
from src.Types import DataType


class TestJsonDataReader:
    @pytest.fixture()
    def valid_json_content(self) -> tuple[str, DataType]:
        """Возвращает строку с валидным JSON и ожидаемый словарь данных."""
        json_string = """
        {
            "Иванов Иван Иванович": {
                "математика": 80,
                "программирование": 90,
                "литература": 76
            },
            "Петров Петр Петрович": {
                "математика": 100,
                "социология": 90,
                "химия": 61
            }
        }
        """
        expected_data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76),
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61),
            ],
        }
        return json_string, expected_data

    def test_read_valid_json(self, tmp_path, valid_json_content):
        """Проверяет корректное чтение валидного JSON-файла."""
        json_string, expected_data = valid_json_content
        file_path = tmp_path / "data.json"
        file_path.write_text(json_string, encoding="utf-8")

        reader = JsonDataReader()
        result = reader.read(str(file_path))

        assert result == expected_data

    def test_read_invalid_json(self, tmp_path):
        """Проверяет, что при некорректном JSON выбрасывается JSONDecodeError."""
        invalid_json = '{"Иванов Иван": {"математика": 80, "литература": 59}'
        file_path = tmp_path / "invalid.json"
        file_path.write_text(invalid_json, encoding="utf-8")

        reader = JsonDataReader()
        with pytest.raises(json.JSONDecodeError):
            reader.read(str(file_path))