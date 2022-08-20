from src.mymodules1.mymodule1 import loader
from unittest.mock import patch, Mock


@patch("src.mymodules1.mymodule1.load_data_file", Mock(return_value="123"))
def test_loader1():
    assert loader() == "123"


@patch("src.mymodules1.mymodule1.load_data_file")
def test_loader2(mock_load_data_from_file):
    mock_load_data_from_file.return_value = "345"
    assert loader() == "345"


def test_loader3():
    with patch("src.mymodules1.mymodule1.load_data_file", Mock(return_value="abcd")):
        assert loader() == "abcd"


def test_loader4(monkeypatch):
    monkeypatch.setattr("src.mymodules1.mymodule1.load_data_file", lambda: "aaa")
    assert loader() == "aaa"
