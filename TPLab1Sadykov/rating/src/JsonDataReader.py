# -*- coding: utf-8 -*-
import json
from DataReader import DataReader
from Types import DataType


class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            raw_data = json.load(file)

        # Ожидаем формат:
        # {
        #   "Иванов Иван": {
        #       "математика": 80,
        #       "литература": 59
        #   },
        #   ...
        # }
        data: DataType = {}

        for student, subjects in raw_data.items():
            data[student] = []
            for subject, score in subjects.items():
                data[student].append((subject, int(score)))

        return data
