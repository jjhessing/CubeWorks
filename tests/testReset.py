import os
import sys
import asyncio

class FileReset():
    """Run FileReset.fullReset() in asyncio to automatically reset all files."""

    FILE_PATHS = [ "TXISR/data/flagsFile.txt" , "TXISR/data/txFile.txt" , "TXISR/data/txWindows.txt" , "flightLogic/backupBootRecords" , "flightLogic/bootRecords" , "flightLogic/data/Attitude_Data.txt" , "flightLogic/data/Deploy_Data.txt" , "flightLogic/data/TTNC_Data.txt" , "TXISR/data/transmissionFlag.txt" , "TXISR/data/AX25Flag.txt"]

    async def reset(self, file_path):
        #opens and erases file, if there is no file, it will create the file
        file = open(file_path, 'w')
        await asyncio.sleep(1)
        if file_path == "flightLogic/backupBootRecords" or file_path == "flightLogic/bootRecords":
            file.write("0\n0\n0\n")
        if file_path == "TXISR/data/flagsFile.txt":
            file.write("0\n0\n0\n0\n0\n")
        if file_path == "TXISR/data/transmissionFlag.txt":
            file.write("Enabled")
        if file_path == "TXISR/data/AX25Flag.txt":
            file.write("Disabled")
        await asyncio.sleep(1)
        file.close() #This closes the file so it is no longer being edited
        await asyncio.sleep(1)

    async def fill(self, i):
        file = open(i, 'a')
        await asyncio.sleep(1)
        file.write("Picanha hamburger flank, biltong shankle tri-tip brisket fatback sausage pig sirloin tail ham venison. Cow bacon kielbasa capicola beef tail ham prosciutto. Doner andouille beef landjaeger, buffalo boudin tail strip steak sirloin cow bacon. Kevin chicken venison ribeye spare ribs strip steak, pig t-bone pork chop meatball bresaola meatloaf landjaeger rump swine. Short ribs pastrami ham meatball.")
        await asyncio.sleep(1)
        file.close()
        await asyncio.sleep(1)
    
    @classmethod
    async def fullReset(self): #Deletes all data files
        await asyncio.gather(
            self.reset(self, self.FILE_PATHS[0]),
            self.reset(self, self.FILE_PATHS[1]),
            self.reset(self, self.FILE_PATHS[2]),
            self.reset(self, self.FILE_PATHS[3]),
            self.reset(self, self.FILE_PATHS[4]),
            self.reset(self, self.FILE_PATHS[5]),
            self.reset(self, self.FILE_PATHS[6]),
            self.reset(self, self.FILE_PATHS[7]),
            self.reset(self, self.FILE_PATHS[8]),
            self.reset(self, self.FILE_PATHS[9])
        )
        print("Done")

    @classmethod
    async def fullFill(self):
        await asyncio.gather(
            self.fill(self, self.FILE_PATHS[0]),
            self.fill(self, self.FILE_PATHS[1]),
            self.fill(self, self.FILE_PATHS[2]),
            self.fill(self, self.FILE_PATHS[3]),
            self.fill(self, self.FILE_PATHS[4]),
            self.fill(self, self.FILE_PATHS[5]),
            self.fill(self, self.FILE_PATHS[6]),
            self.fill(self, self.FILE_PATHS[7]),
            self.fill(self, self.FILE_PATHS[8]),
            self.fill(self, self.FILE_PATHS[9])
        )
        print("Done")

asyncio.run(FileReset.fullReset())