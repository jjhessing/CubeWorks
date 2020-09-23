import os
import sys
from pathlib import Path

base = Path(__file__).parent #sets base as the current file directory
file_path = (base / "resetText.txt").resolve()#sets the file path to the base
file = open(file_path, 'r+') #opens the file using the file path
file.truncate(0) #This is to delete everything
file.close() #This closes the file so it is no longer being edited
print("We ran") #Shows that the program is finished