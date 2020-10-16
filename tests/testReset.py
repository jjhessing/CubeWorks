import os
import sys

class FileReset():
    """ This will automatically clear all data files and reset other needed files as though the pi was just beginning to boot up. Takes no input. """
    
    FILE_PATHS = [ "TXISR/data/flagsFile.txt" , "TXISR/data/txFile.txt" , "TXISR/data/txWindows.txt" , "flightLogic/backupBootRecords" , "flightLogic/bootRecords" , "flightLogic/data/Attitude_Data.txt" , "flightLogic/data/Deploy_Data.txt" , "flightLogic/data/TTNC_Data.txt" , "TXISR/data/transmissionFlag.txt" , "TXISR/data/AX25Flag.txt"]

    #I'm 95% sure this is what you wanted, with all of the code being in __init__ so that it will automatically run if the class is called, however I kept the code we originally wrote where we divided them into different functions down below
    def __init__(self):
        for i in self.FILE_PATHS: #Loops for each file in list
            try:
                #opens and erases file, if there is no file, it will create the file
                file = open(i, 'w') 
            except SyntaxError: #I still have both of these exceptions here, but I'm not sure if they're needed
                print("There was a syntax error and we should re run the program")
            except OSError:
                print("Not gonna lie not sure what would cause this one")
            else: #All of these if statements are simply to rewrite the text for the different records that need to be re-written and not just erased
                if i == "flightLogic/backupBootRecords" or i == "flightLogic/bootRecords":
                    file.write("0\n0\n0\n")
                if i == "TXISR/data/flagsFile.txt":
                    file.write("0\n0\n0\n0\n0\n")
                if i == "TXISR/data/transmissionFlag.txt":
                    file.write("Enabled")
                if i == "TXISR/data/AX25Flag.txt":
                    file.write("Disabled")
                file.close() #This closes the file so it is no longer being edited
        print("Done")

#This is what we originally wrote
"""
    def fileReset(self, file_path):
        try:
            #opens and erases file, if there is no file, it will create the file
            file = open(file_path, 'w') 
        except SyntaxError: #I still have both of these exceptions here, but I'm not sure if they're needed
            print("There was a syntax error and we should re run the program")
        except OSError:
            print("Not gonna lie not sure what would cause this one")
        else:
            if file_path == "flightLogic/backupBootRecords" or file_path == "flightLogic/bootRecords":
                file.write("0\n0\n0\n")
            if file_path == "TXISR/data/flagsFile.txt":
                file.write("0\n0\n0\n0\n0\n")
            if file_path == "TXISR/data/transmissionFlag.txt":
                file.write("Enabled")
            if file_path == "TXISR/data/AX25Flag.txt":
                file.write("Disabled")
            file.close() #This closes the file so it is no longer being edited
    @classmethod
    def fullReset(self): #Deletes all data files
        for i in self.FILE_PATHS:
            self.fileReset(self,i)      
        print("Done")


    @classmethod
    def fullFill(self):
        for i in self.FILE_PATHS:
            file = open(i, 'a')
            file.write("Picanha hamburger flank, biltong shankle tri-tip brisket fatback sausage pig sirloin tail ham venison. Cow bacon kielbasa capicola beef tail ham prosciutto. Doner andouille beef landjaeger, buffalo boudin tail strip steak sirloin cow bacon. Kevin chicken venison ribeye spare ribs strip steak, pig t-bone pork chop meatball bresaola meatloaf landjaeger rump swine. Short ribs pastrami ham meatball.")
            file.close()
        print("Filled")
"""