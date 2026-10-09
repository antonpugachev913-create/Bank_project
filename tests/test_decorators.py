import pytest

from src.decorators import log


def test_decorators(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    logi = capsys.readouterr()
    assert logi.out == "my_function ok\n"

    with pytest.raises(TypeError):
        my_function(1, "2")
    logi = capsys.readouterr()
    assert logi.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"


def test_log_to_file(tmp_path) -> None:
    test_file = tmp_path / "test_log.txt"

    @log(filename=str(test_file))
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3
    with pytest.raises(TypeError):
        my_function(1, "2")

    with open(test_file, "r", encoding="utf-8") as f:
        file_content = f.read()

    expected_logs = (
        "my_function ok\n" "my_function error: TypeError. Inputs: (1, '2'), {}\n"
    )
    assert file_content == expected_logs
