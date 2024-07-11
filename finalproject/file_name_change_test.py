from file_name_change import log_changes
from datetime import datetime
import pytest

current_time = datetime.now(tz=None)
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

def test_log_changes():
    assert log_changes("testnameold.txt", "testnamenew.txt") == "Change made: testnameold.txt -> testnamenew.txt at " + current_time + "\n"

test_log_changes()