from src.mymodules1.mymodule2 import load_data_file
from unittest.mock import patch, Mock


@patch(
    "src.mymodules1.mymodule2.resource_stream",
    Mock(return_value=Mock(read=Mock(return_value="abc123".encode()))),
)
def test_load_data_file():
    assert load_data_file() == "abc123"
