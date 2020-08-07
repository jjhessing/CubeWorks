#Shawn's pre review notes:
# Time here is declared as an int, I would not do that beacuse it could overflow. Just let python handle it. 
# Also when this class gets called by flight logic it will pass it an object that will handle getting the data we have stored.
# Inturrupt requires Pin

# from machine import Pin
# from multiprocessing import Process
from datetime import datetime
import time
import calendar
import os
import string
import sys
#import asycnio
import rxHandling

class INTERRUPT:

    #change all functions to self
    #change class variables to self

    # file with tx windows and durations. Eachline should have <timestamp of start of tx window> <duration of window>
    TX_WINDOWS_FILE = "data/TxWindows.txt"

    def __init__(self):
        '''
        start two infinitely running functions
        '''
        sys.stdout.write("Im in the main function, all you should use is sys")
        print("Im in the main function")
        #Comment out other function until asynio works in function
       # self.watchTxWindows()
        self.watchReceptions()
        # Code that runs
        self.TRANSMIT_EXE = "TXServiceCode/TXService.run"

        # Code that scans the UART
        self.READ_EXE = "TXServiceCode/watchRX.run"

        '''
        p1 = Process(target=watchTxWindows)
        p1.start()
        p2 = Process(target=inturruptWatchReceptions)
        p2.start()
        p1.join()
        p2.join()
        '''

    '''
    START PROCESS 1 (p1) DEFINITION 
    '''
    # asyncio def watchTxWindows():
    def watchTxWindows(self):
        '''
        watch windows and call to transmit if within window.
        '''
        print("im in the watch TX WINDOWS... shouldn't be here..")

        # get current time
        current_time = int(time.time())

        f = open(self.TX_WINDOWS_FILE, 'r')

        nextTimeFound = False

        # Should be an infinite loop
        while nextTimeFound == False:
            line = fp.readline()
            line = line.replace('\n','')
            line = line.split(' ')
            if line[0] == '':
                print("no TX window is listed. FAILING...")
            if current_time < int(line[0]):
                delay = (int(line[0]) - int(current_time))
                if delay < 0:
                    print("Something went bad, cannot have negative wait time")
                time.sleep(delay - 5)

                dataTypeWithSpace = " "+line[1]
                callRadioDriver(dataTypeWithSpace)
        f.close()
        #await asyncio.sleep(1)

    def callRadioDriver(self, dataType):
        '''
        Function that calls TX EXE
        '''
        # FNULL = open(os.devnull, 'w')
        os.system(self.TRANSMIT_EXE+dataType)

    '''
    END PROCESS 1 DEFINITION
    '''

    '''
    START PROCESS 2 (p2) DEFINITION
    '''
    #asyncio def watchReceptions():
    def watchReceptions(self):
        print("im in the watchReceptions function! that's good")
        checking = os.system(READ_EXE)

        print("why didn't I get in the loop?")
        while checking <= 0:
            # print("im in the loop")
            #print("checking: " + str(checking))
            checking = os.system(self.READ_EXE)
            if checking > 0:
                print("should now call TXISR rxHandling")
                x = rxHandling.TXISR(self.checking)
        # wait ayncio.sleep(1)
    '''
    END PROCESS 2 DEFINITION
    '''

'''
Depricated Functions:


#this class handles the tx files
class txWindows
    def __init__(self, startTime)
        self.tx = open(txSchedual)
        self.startTime = startTime

    #this func will add the window to our tx file
    def creatTXSchedual(self, schedual):
        self.tx.append(schedual)

    def waitForTx(self):
        window = self.tx.readline
        while((self.startTime + time.time()) != window)
        {}
        
async def inturruptWatchReceptions():
    #TODO: get the correct pin for the radio connection. 1.5-1.8 voltage
    btn = Pin(0, Pin.IN)

    # Create inturrupt
    btn.irq(callRxHandeling(btn))
    

def callRxHandeling(btn):
    # If data comes across pins, call rxHandeling to process incomming data
    if btn.value() >= CONST_VOLTAGE
       x = rxHandling.TXISR()

'''
