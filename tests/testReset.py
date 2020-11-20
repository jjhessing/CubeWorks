import os
import sys
import asyncio

class FileReset():
    """Checks to ensure that data files exist after reboot. Use "asyncio.run(FileReset.fullReset())" to run.
    
    Includes program to manually reset individual files for testing purposes. Use "asyncio.run(FileReset.fullReset())" to run."""

    #List of file paths
    FILE_PATHS = [ 
        "TXISR/data/flagsFile.txt" , 
        "TXISR/data/txFile.txt" , 
        "TXISR/data/txWindows.txt" , 
        "TXISR/data/transmissionFlag.txt" , 
        "TXISR/data/AX25Flag.txt",
        "flightLogic/backupBootRecords" , 
        "flightLogic/bootRecords" , 
        "flightLogic/data/Attitude_Data.txt" , 
        "flightLogic/data/Deploy_Data.txt" , 
        "flightLogic/data/TTNC_Data.txt" ,]

    def reset(self, file_path):
        """Opens and erases file, certain files are then filled with required text. If there is no file under a certain file path, it will create the file."""
        #Depending on the file path, replaces the empty file with a string of text based on what data will be written in the file
        file = open(file_path, 'w')
        if file_path == "flightLogic/backupBootRecords" or file_path == "flightLogic/bootRecords":
            file.write("0\n0\n0\n")
        if file_path == "TXISR/data/flagsFile.txt":
            file.write("0\n0\n0\n0\n0\n")
        if file_path == "TXISR/data/transmissionFlag.txt":
            file.write("Enabled")
        if file_path == "TXISR/data/AX25Flag.txt":
            file.write("Disabled")
        file.close()
        #This closes the file so it is no longer being edited
    
    @classmethod
    async def fullReset(self):
        """Checks to make sure that files necessary for reboot exist, if they don't, it creates them."""
        #Runs through every file in FILE_PATHS list.
        for i in self.FILE_PATHS:
            #Opens the file to see if it exists.
            try:
                file = open(i)
            #If it doesn't, it runs reset to create it.
            except OSError:
                self.reset(self, i)
                print("Created " + i)
                await asyncio.sleep(0)
            #Otherwise it just closes the file.
            else:
                file.close()
                await asyncio.sleep(0)

    @classmethod
    async def individualReset(self, file_path):
        """Allows the manual reset of a single file."""
        #Runs reset once for a single file.
        self.reset(self, file_path)
        await asyncio.sleep(0)

asyncio.run(FileReset.fullReset())