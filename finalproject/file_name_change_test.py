from file_name_change import directory_fix, change_single_file_name
from file_name_change import *

from datetime import datetime
import pytest


current_time = datetime.now(tz=None)
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

def test_directory_fix():
    #test that the directory is fixed correctly
    assert directory_fix("testnameold.txt", "testfolder") == "./testfolder/testnameold.txt"

def test_change_single_file_name():
    #test that the file name is changed correctly and raises an error if error occurs
    pytest.raises(FileNotFoundError, change_single_file_name,"./testingfolder/testnameold.txt", "./testfolder/testnameold.txt")

def test_grab_inputs():
    #test that the inputs are grabbed correctly
    assert grab_inputs("testnameold.txt", "testnamenew.txt", "testfolder") == ("testnameold.txt", "testnamenew.txt", "testfolder")



pytest.main(["-v", "--tb=line", "-rN", __file__])
