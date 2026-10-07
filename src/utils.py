import json
from json import load
from pathlib import Path
def get_transaction_information(way):
    file_path = Path(way)
    if not file_path.exists() or file_path.stat().st_size == 0:
        return []
    with open(way, 'r') as file:
        out = load(file)
        if isinstance(out, list):
            return []
        return out


