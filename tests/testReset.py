import os
import sys
# Change this function to a class
# Add exception cases DONEish
# Edit class so that it will reset every file if need be -> array thingy
FILE_PATHS = [ "TXISR/data/flagsFile.txt" , "TXISR/data/txFile.txt" , "TXISR/data/txWindows.txt" , "flightLogic/backupBootRecords" , "flightLogic/bootRecords" , "flightLogic/data/Attitude_Data.txt" , "flightLogic/data/Deploy_Data.txt" , "flightLogic/data/TTNC_Data.txt" , "TXISR/data/transmissionFlag.txt" , "TXISR/data/AX25Flag.txt"]
def fileReset(file_path):
    try:
        #opens and erases file, if there is no file, it will create the file
        file = open(file_path, 'w') 
        if file_path == "flightLogic/backupBootRecords" or file_path == "flightLogic/bootRecords":
            file.write("0\n0\n0\n")
        if file_path == "TXISR/data/flagsFile.txt":
            file.write("0\n0\n0\n0\n0\n")
        if file_path == "TXISR/data/transmissionFlag.txt":
            file.write("Enabled")
        if file_path == "TXISR/data/AX25Flag.txt":
            file.write("Disabled")
        
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
    for i in FILE_PATHS:
        fileReset(i)      
    print("Done")



def fullFill():
    for i in FILE_PATHS:
        file = open(i, 'a')
        file.write("Picanha hamburger flank, biltong shankle tri-tip brisket fatback sausage pig sirloin tail ham venison. Cow bacon kielbasa capicola beef tail ham prosciutto. Doner andouille beef landjaeger, buffalo boudin tail strip steak sirloin cow bacon. Kevin chicken venison ribeye spare ribs strip steak, pig t-bone pork chop meatball bresaola meatloaf landjaeger rump swine. Short ribs pastrami ham meatball.")
        file.close()

fullReset()