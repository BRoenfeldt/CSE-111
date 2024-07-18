from file_name_change import directory_fix, change_single_file_name
from file_name_change import grab_inputs, log_changes
from datetime import datetime
import pytest


current_time = datetime.now(tz=None)
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

def test_directory_fix():
    #test that the directory is fixed correctly
    assert directory_fix("testnameold.txt", "testfolder") == "./testfolder/testnameold.txt"
    assert directory_fix("other.pdf", "MyPDFs") == "./MyPDFs/other.pdf"

def test_change_single_file_name():
    #test that the file name is changed correctly and raises an error if error occurs
    pytest.raises(Exception, change_single_file_name,"./asdf/asdf.txt", "./asdf/asdfg.txt")

def test_grab_inputs():
    #test that the inputs are grabbed correctly
    assert grab_inputs("testnameold.txt", "testnamenew.txt", "testfolder") == ("testnameold.txt", "testnamenew.txt", "testfolder")    
    assert grab_inputs() == ("Old File Name - ex: class_notes.txt", "New File Name - ex: CSE11_notes.txt", "Directory - ex: myFiles/importantFiles (Must be in the same folder as where this script is ran)")

def test_log_changes():
    assert log_changes("testnameold.txt", "testnamenew.txt") == None
    assert log_changes("", "") == None

pytest.main(["-v", "--tb=line", "-rN", __file__])
