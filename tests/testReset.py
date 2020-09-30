import os
import sys

def fileReset(file_path): 
    file = open(file_path, 'r+') #opens the file using the function input
    file.truncate(0) #This is to delete everything
    file.close() #This closes the file so it is no longer being edited
def dataReset(): #Deletes all data files
    fileReset("flightLogic/data/Attitude_Data.txt") 
    fileReset("flightLogic/data/Deploy_Data.txt")
    fileReset("flightLogic/data/TTNC_Data.txt")