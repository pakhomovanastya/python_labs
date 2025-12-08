import pytest
import json
from pathlib import Path
from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json


def test_students_from_json(tmp_path: Path):
    src = tmp_path / "students_input.json"
    data = [
        {"fio": "Петя",
        "birthdate": "2008/07/12",
        "group": "BI-6",
        "gpa": 4.6},
        {"fio": "Маша",
        "birthdate": "2004/12/1",
        "group": "LD-6",
        "gpa": 3.7}
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    studentiki = students_from_json(str(src))
    assert len(studentiki) == 2
    assert isinstance(studentiki[0], Student)