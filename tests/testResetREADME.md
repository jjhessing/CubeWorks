GASPACS Software : testReset.py
==
Opening Notes:
--
When something goes wrong enough for the pi to reset a check needs to be done to ensure that the data files exist and create them if it does not. This program will do just that, running through a set list of programs, checking to ensure the exist, and creating them if they do not. 

Testing:
--
Location: 
--
/tests/testReset.py

Full Reset:

Functionality:
--
    The files that will need to be reset periodically while the satilite is in space are:

    *TXISR/data/flagsFile.txt
    TXISR/data/txFile.txt
    TXISR/data/txWindows.txt
    *TXISR/data/transmissionFlag.txt 
    *TXISR/data/AX25Flag.txt
    *flightLogic/backupBootRecords
    *flightLogic/bootRecords
    flightLogic/data/Attitude_Data.txt
    flightLogic/data/Deploy_Data.txt
    flightLogic/data/TTNC_Data.txt

    * files have strings added to them after being reset for proper functionality.

    The program runs through the list of files trying to open each one. If the file does not exist then an OS error will be thrown which the except clause will catch and reopen the file using the 'w' argument which creates the file when it's not found.

Questions:
--
Where does this program run?
Do we need to incorporate this program into some other program?