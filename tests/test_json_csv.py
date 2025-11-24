import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    """Позитивный тест: корректная конвертация JSON → CSV"""
    # tmp_path - встроенная фикстура pytest для работы с временными файлами
    # создаем пути к временным файлам
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    # записываем тестовые данные в JSON файл
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))
    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))  # читаем CSV как список словарей
    # проверяем утверждения
    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_json_to_csv_wrong_file(tmp_path: Path):
    "Негативный тест: неверное расширение файла"
    with pytest.raises(ValueError):  # ожидаем, что функция выбросит ValueError
        src = tmp_path / "people.txt"
        dst = tmp_path / "people.csv"
        json_to_csv(str(src), str(dst))


def test_json_to_csv_with_out_dict(tmp_path: Path):
    "Негативный тест: JSON с неправильной структурой данных"
    # JSON файл содержит список чисел вместо списка словарей
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(
        json.dumps([1, 2, 3, 4], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_empty(tmp_path: Path):
    "Негативный тест: обработка пустого JSON файла"
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(json.dumps([], ensure_ascii=False, indent=2), encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_incorrect_json(tmp_path: Path):
    "Негативный тест: некорректный синтаксис JSON файла"
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text("Одинцово", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_roundtrip(tmp_path: Path):
    """Позитивный тест: корректная конвертация CSV → JSON"""
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    # создаем корректный CSV файл с заголовком и данными
    src.write_text("name,age,city\nAlice,22,SPB\nBob,25,Moscow")
    csv_to_json(str(src), str(dst))
    with dst.open(encoding="utf-8") as f:
        rows = json.load(f)
    assert len(rows) == 2
    assert {"name", "age", "city"} <= set(rows[0].keys())


def test_csv_to_json_wrong_file(tmp_path: Path):
    "Негативный тест: неверное расширение файла для CSV → JSON"
    with pytest.raises(ValueError):
        src = tmp_path / "people.txt"
        dst = tmp_path / "people.json"
        csv_to_json(str(src), str(dst))


def test_csv_to_json_none(tmp_path: Path):
    "Негативный тест: обработка отсутствующего CSV файла"
    with pytest.raises(FileNotFoundError):
        src = "people.csv"  # Файл, которого нет в файловой системе
        dst = tmp_path / "people.json"
        csv_to_json(str(src), str(dst))


def test_csv_to_json_empty(tmp_path: Path):
    "Негативный тест: обработка пустого CSV файла"
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))

