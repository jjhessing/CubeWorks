import os
import sys

def fileReset(file_path):
    try:
        #opens and erases file, if there is no file, it will create the file
        file = open(file_path, 'w') 
    except FileNotFoundError:
        print("Uh oh spaghettios, if this is happening we're all screwed.")
    except SyntaxError:
        print("There was a syntax error and we should re run the program")
        print(" because if this is happening in space it just means a bit error")
    except OSError:
        print("Not gonna lie not sure what would cause this one")
    else:
        file.close() #This closes the file so it is no longer being edited
def fullReset(): #Deletes all data files
    fileReset("flightLogic/data/Attitude_Data.txt")
    fileReset("flightLogic/data/Deploy_Data.txt")
    fileReset("flightLogic/data/TTNC_Data.txt")

fileReset("tests/resetText.txt")