#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <time.h>
#include <fcntl.h>
#include <termios.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <stdint.h>
//Take just the DEBUG line out when your are done debugging and leave debug.h
#define DEBUG
#include "debug.h"

//enable and disable are set up in the make file,
#define ENABLE "./configPinsTXISR"
#define DISABLE "./configPinsTXISRDone"

#define FLAG_FILE "../TXISR/data/flagsFile.txt" //change this later for the real program
#define FORMAT_FILE "../TXISR/data/txFile.txt" //this is the file that dallan will creat
#define UART_PORT "/dev/serial0" //this is serial port name, make sure this is correct for the final code

//this is our time delay
#define DELAY_tx 120

//this defines are for the data types
#define MAX_BYTES_PER_LINE 256
#define MAX_NUM_OF_DATA_TYPES 5
#define DELAY_UNTIL_TX_WINDOW 5000
#define SIZE_OF_TIME_STAMP 10
#define PHOTO_TYPE 3
#define TIME_DEVISOR ':'

//NOTE: becasue of how we have to set the boud rate I cannot use a define for it in ceritian places, just do a contrl f and look for BOUD_RATE
//it is place next to every place that the boud rate is used, you also need to change the define as it is used as well.
//NOTE: this boud rate (9600) is the radio speed. We talk to it with a diffrent speed, in other words the 9600 is our divisor for the delay
#define BOUD_RATE 9600

int changeCharToInt(char a);

//this sets control of the settings for our serial port
struct termios options;

void setUpUart();
char convertCharToHex (char lowByte, char highByte);

//returns ms since the epoch
intmax_t millis()
{
    struct timespec current_time;
    clock_gettime(CLOCK_MONOTONIC_RAW, &current_time);
    //get the milli seconds
    intmax_t a = ((current_time.tv_sec) * 1000) + ((current_time.tv_nsec) / 1000000);
    return a;
}



/*******************************************************************************************
 * sudo code: Main
 * this first tries to open the file it is trying to send
 * then it tries to take control of the serial ports
 * then it tries to open the serial port
 * then it reads each line of the file and sends it one at a time
 *      NOTE: the program will wait x number of millaseconds inbetween each line it sends
 *            depending on what the radio needs
 * After it has sent everything it opens the flags file and records the time of the last
 *      sent record
 * It then closes the serial port
 * it then returns control back to linuxs
 * Program then exits
 *******************************************************************************************/
void main(int argc,char* argv[])
{
    /////TODO/////
    /*
    *debug the time check on transmissionWindow 
    *debug the wait after each transmission 
    *Write the time to the flags file
    *Add in any set up commucation to the radio
    * TEST, UART, and the bash commands
    */
    intmax_t startTime = millis();
    intmax_t currentTime = millis();
    intmax_t startTimeTX = 0;
    intmax_t currentTimeTX = 0;
    //gather user input
    int dataType = changeCharToInt(*argv[1]);
    int transmissionWindow = 0;
    char sendingData[(MAX_NUM_OF_DATA_TYPES / 2)] = {0}; 
    

    FILE *txFile;
    if (!(txFile = fopen(FORMAT_FILE,"r")))
    {
        //if we fail exit
        DEBUG_P(Failed to open file)
        exit(1);
    }

    FILE *recordFile;
    if (!(recordFile = fopen(FLAG_FILE,"r+")))
    {
        //if we fail exit
        DEBUG_P(Failed to open the flags file)
        exit(1);
    }

    //this is where we will store the last transmission
    //5 data types
    long flags[MAX_NUM_OF_DATA_TYPES];
    //pop the data types
    DEBUG_P(opening file)
    //NOTE: WE HAVE TO MAKE THE FLAGS FILE RIGHT OR WE WILL GET SYSTEM FALUIR.
    for (int i =0; i < MAX_NUM_OF_DATA_TYPES; i++)
    {
      fscanf(recordFile, "%ld", &flags[i]);  
      PRINT_TIME(flags[i]);
    }

    //open the serial ports
    //NOTE: opening the serial port clears the buffer!!!
    int txPort = open(UART_PORT, O_RDWR | O_NOCTTY ); 
    if (txPort == -1)
    {
        printf ("Error no is : %d\n", errno);
        printf("Error opening serial port\n");
        exit(1);
    }
    //set up the uart 
    setUpUart();

    //read in all the lines of a file
    char ch = 1;
    //set up array for tx, the max is 256, so we better not exceed that anyways so using an array of 256 is fine.
    char line[MAX_BYTES_PER_LINE] = {0};
    char timeStamp[SIZE_OF_TIME_STAMP];
    //get tx time
    fscanf(txFile, "%d", &transmissionWindow);
    PRINT_DEBUG(transmissionWindow)
    fgetc(txFile);
    currentTime = millis();
    
    DEBUG_P(Waiting for tx window>>>)
    //this is where we wait until we hit 5 seconds after this code has been called
    while((currentTime - startTime) < DELAY_UNTIL_TX_WINDOW)
    { 
        currentTime = millis();
    }
    DEBUG_P(current Time - Start Time:)
    PRINT_TIME(currentTime - startTime)

    //Send command to put the local radio into pipe mode
    write(txPort, "ES+W22003321\r", 13);
    //Sleep for 1 second to allow time to go into pipe mode
    sleep(1);
    //Transmit command to put the remote radio into pipe mode
    write(txPort, "ES+W23003321\r", 13);
    //Sleep for 1 second to allow time to go into pipe mode
    sleep(1);

    while(!feof(txFile))
    {
       //this checks the transmission window
        currentTime = millis();
        //break if we have passed the tx window
        if((currentTime - startTime) > transmissionWindow) 
        {
            DEBUG_P(\nEnding>>>)
            break;
        }

        
        DEBUG_P(current Time - Start Time:)
        PRINT_TIME(currentTime - startTime)
        DEBUG_P(\nSending>>>)
        //get the size of each line in the file
        int charCount = 0;
        int end = 0;
        int charTimeCount = 0;
        for (int i = 0; i < MAX_BYTES_PER_LINE; i++)
        {
            line[i] = '0';
        }
        
        //DEBUG_P(Im in the main loop)

        do 
        {
            if(feof(txFile)) break;
            ch = fgetc(txFile);
            //this collects the time stamp
            if(!end && !feof(txFile))
            {
                timeStamp[charTimeCount++] = ch;
                //PRINT_DEBUG_c(ch)
            }
            if (ch == TIME_DEVISOR)
            {
                end = 1;
                //if you dont wanna send the : uncommit the next line into the code
                //continue;
            }
            //save all the data in that line
            //this if lets us not send the line number if this is a photo file
            if(end && ch != TIME_DEVISOR && ch != 10) 
            {
                line[charCount++] = convertCharToHex(fgetc(txFile), ch);
                //PRINT_DEBUG_c(ch)
                //PRINT_DEBUG(charCount)
            }
            //DEBUG_P(Im in the sub loop)
        }while(ch != '\n' && !feof(txFile));
        
        
        //DEBUG_P(leaving loop)

        if(ch == '\n' || feof(txFile))
        {
            //transmit the data
            #ifdef DEBUG
                for(int i = 0; i < charCount; i++)
                {
                    printf("%X", line[i]);
                    if (line[i] == 0) {
                        PRINT_DEBUG_CHAR('0')
                    }
                }
                PRINT_DEBUG_CHAR('\n')
            #endif
            //this line of code sends things out on the tx line
            //start the transmition time
            startTimeTX = millis();
            currentTimeTX = 0;
            write(txPort, line, charCount);
            //this will let us print to the file
            int written = 0;
            //this stores the last sent data time
            flags[dataType] = atoi(timeStamp);
            //delay the right amount of time for the radio, 120 millisecod + the amount of bytes / by the boud_rate, in almost 
            //cause this will make no diffrence.
            //this stores the last sent data time
            flags[dataType] = atoi(timeStamp);
            //PRINT_LONG(flags[dataType])
            //delay the right amount of time for the radio, 120 millisecod + the amount of bytes / by the boud_rate, in almost 
            //cause this will make no diffrence. 
            while((currentTimeTX - startTimeTX) < DELAY_tx + (charCount / BOUD_RATE))
            { 
                currentTimeTX = millis();
                if(!written)
                {
                    
                        //delete the existing data
                        //fclose(recordFile);
                        if (recordFile = fopen(FLAG_FILE,"w"))
                        {
                            //if succesfull we will print it and set the written to true else we will try again.
                            //reprint it
                            //print the last sent time
                            for(int g = 0; g < MAX_NUM_OF_DATA_TYPES; g++)
                            {
                                fprintf(recordFile, "%ld\n", flags[g]);
                            }
                            //set written to true
                            written = 1;
                        }
                        //if we fail recreate the file
                        else
                        {
                            remove(FLAG_FILE);
                            //recreate the file
                            recordFile = fopen(FLAG_FILE,"w");
                            for(int g = 0; g < MAX_NUM_OF_DATA_TYPES; g++)
                            {
                                fprintf(recordFile, "%ld\n", flags[g]);
                            }
                            //set written to true
                            written = 1;
                        }
                    //delete the existing data
                    fclose(recordFile);
                }
                sleep((DELAY_tx + (charCount / BOUD_RATE))/1000);
            }
            charCount = 0;
            DEBUG_P(TX end Time: )
            PRINT_TIME(currentTimeTX)
            DEBUG_P(TX end start Time: )
            PRINT_TIME(startTimeTX)
            DEBUG_P(Delta T: )
            PRINT_TIME(currentTimeTX - startTimeTX)
        }
    } 

     //give control of the port back to linuxs
    //  int disable = system(DISABLE);
    //  //if we fail reboot
    //  if(disable != 0) 
    //  {
    //      DEBUG_P(Failed to release tx uart pin)
    //      exit(1);
    //  } 
}

/*******************************************************************************************
 * setUpUart
 * this func sets up the uart commincation for us so everything works nicely
 *******************************************************************************************/
void setUpUart()
{
    //set the baud rate, it is the number with a b infornt of it ex 115200 -> B115200
    //BOUD_RATE
    cfsetspeed(&options, B115200);

    //set up the number of data bits
    options.c_cflag &= ~CSIZE;
    options.c_cflag |= CS8;
}

/*******************************************************************************************
 * setUpUart
 * this func will convert a char in to an int (works for 0 though 9 and a - f)
 * if it fails to convert the vaule it exits the program and sends an error message.
 *******************************************************************************************/
int changeCharToInt(char a)
{
    switch(a)
    {
        //use assci table to decode this part of the code
        case 48:
            return 0;
        case 49:
            return 1;
        case 50:
            return 2;
        case 51:
            return 3;
        case 52:
            return 4;
        case 53:
            return 5;
        case 54:
            return 6;
        case 55:
            return 7;
        case 56:
            return 8;
        case 57:
            return 9;
        case 'a':
            return 10;
        case 'b':
            return 11;
        case 'c':
            return 12;
        case 'd':
            return 13;
        case 'e':
            return 14;
        case 'f':
            return 15;
        default :
            {
                DEBUG_P(invaild data type)
                PRINT_DEBUG_c(a)
                exit(1);
            }
    }
}
/*******************************************************************************************
 * Convertto hex
 * this func will convert a char in to hex 
 * if it fails to convert the vaule it exits the program and sends an error message.
 * it returns the int value
 *******************************************************************************************/
char convertCharToHex (char lowByte, char highByte)
{
    //convert to ints
    char low = changeCharToInt(lowByte);
    char high = changeCharToInt(highByte);
    //shift high and add it to low.
    char new = low + (high << 4);
    return new;
}
