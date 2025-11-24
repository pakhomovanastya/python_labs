import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    """Позитивный тест: корректная конвертация JSON → CSV"""
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_json_to_csv_wrong_file(tmp_path: Path):
    with pytest.raises(ValueError):
        src = tmp_path / "people.txt"
        dst = tmp_path / "people.csv"
        json_to_csv(str(src), str(dst))


def test_json_to_csv_with_out_dict(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(
        json.dumps([1, 2, 3, 4], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_empty(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(json.dumps([], ensure_ascii=False, indent=2), encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_incorrect_json(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text("Одинцово", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_roundtrip(tmp_path: Path):
    """Позитивный тест: корректная конвертация CSV → JSON"""
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age,city\nAlice,22,SPB\nBob,25,Moscow")
    csv_to_json(str(src), str(dst))
    with dst.open(encoding="utf-8") as f:
        rows = json.load(f)
    assert len(rows) == 2
    assert {"name", "age", "city"} <= set(rows[0].keys())


def test_csv_to_json_wrong_file(tmp_path: Path):
    with pytest.raises(ValueError):
        src = tmp_path / "people.txt"
        dst = tmp_path / "people.json"
        csv_to_json(str(src), str(dst))


def test_csv_to_json_none(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        src = "people.csv"
        dst = tmp_path / "people.json"
        csv_to_json(str(src), str(dst))


def test_csv_to_json_empty(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


# def test_csv_to_json_not_headers(tmp_path: Path):
#     src = tmp_path / "people.csv"
#     dst = tmp_path / "people.json"
#     src.write_text("name,age\nAlice,22,SPB\nBob,25,Moscow")
#     with pytest.raises(ValueError):
#         csv_to_json(str(src), str(dst))
