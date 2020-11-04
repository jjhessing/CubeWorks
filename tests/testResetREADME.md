GASPACS Software : testReset.py
==
Opening Notes:
--
When the satilite is in orbit, there will not be enough data storage on the satilite to continually store more and more data without a generic data reset class. When the data is taking up a certain portion of the total avaliable storage on the satilite, and after all data has been transferred back to ground, there needs to be a way to reset all of these files while the satilite is in orbit. 

Testing:
--
Location: 
--
Functionality:
--
The files that will need to be reset periodically while the satilite is in space are:

*TXISR/data/flagsFile.txt
 TXISR/data/txFile.txt
 TXISR/data/txWindows.txt
*flightLogic/backupBootRecords
*flightLogic/bootRecords
 flightLogic/data/Attitude_Data.txt
 flightLogic/data/Deploy_Data.txt
 flightLogic/data/TTNC_Data.txt
*TXISR/data/transmissionFlag.txt 
*TXISR/data/AX25Flag.txt

The stared files are those which need to have certain strings added in after the files have been completely reset, resetFile.py does this. This class also runs asynchronously, meaning that this class can be called even if another asynchronous program is running, this one can run too.

Questions:
--
Why does this need to run asynchronously?
Where does this program run asynchronously?
Do we need to have a safety system in place to prevent this class from being run accidentaly before all of the data is transfered back to ground?

