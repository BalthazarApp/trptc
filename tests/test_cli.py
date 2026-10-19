import pytest

from trptc.__main__ import main


@pytest.mark.parametrize(
    "operation, expected",
    [
        ("sum", "5"),
        ("multiply", "6"),
        ("subtract", "-1"),
        ("divide", "0.6666666666666666"),
        ("power", "8"),
    ],
)
def test_operations(operation, expected, capsys):
    assert main([operation, "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == expected


def test_int_vs_float_parsing(capsys):
    assert main(["sum", "1", "2"]) == 0
    assert capsys.readouterr().out.strip() == "3"
    assert main(["sum", "1.5", "2"]) == 0
    assert capsys.readouterr().out.strip() == "3.5"


def test_divide_by_zero(capsys):
    assert main(["divide", "1", "0"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "division by zero" in captured.err


def test_unknown_operation():
    with pytest.raises(SystemExit) as excinfo:
        main(["modulo", "1", "2"])
    assert excinfo.value.code == 2
