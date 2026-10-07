import json
from json import load
from pathlib import Path


def get_transaction_information(way):
    try:
        file_path = Path(way)
        if not file_path.exists() or file_path.stat().st_size == 0:
            return []
        with open(way, "r", encoding="utf-8") as file:
            out = load(file)
            if not isinstance(out, list):
                return []
            return out
    except json.JSONDecodeError:
        return []
