from file_name_change import change_single_file_name
from datetime import datetime
import pytest

current_time = datetime.now(tz=None)
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

def test_change_single_file_name():
    assert change_single_file_name("testnameold.txt", "testfolder") == "testfolder/testnameold.txt"

test_change_single_file_name()