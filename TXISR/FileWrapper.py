
FILE_TYPES = {
    ".data" : 0,
    ".transmission" : 1,
}


class FileWrapper():
    """
    File Wrapper class to deal with file based exceptions and handling for primary use in the USU GASPACS Cubesat software. To open a file call the constructor FileWrapper(filename,mode,encoding)
    """


    def __init__(self,filename,mode,encoding):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.closed
        self.fileType = self.getFileType()
        self.file = self.openFile(self.__filename,self.__mode,self.__encoding)


    def openFile(self):
        """
        Trys to open the file specified in class constructor. Handles the exceptions as needed.
        """
        try:
            #try to return a file object
            f = open(self.__filename,mode=self.__mode,encoding=self.__encoding)
            self.closed = f.closed
            return f

        #catch all the exceptions 
        except FileNotFoundError as fileNotFound:
            pass
            #TODO:logic for handling based on file type
        except FileExistsError as fileExists:
            pass
            #TODO:logic for handling based on file type
        except OSError as osError:
            pass
            #TODO:logic for handling based on file type
        except Exception as exception:
            pass
            #TODO:logic for handling based on file type
        finally:
            pass


    def getFileType(self):
            """
            Takes the file type of the file specified in the constructor and looks it up in a const dict of file types and returns an int for use in deciding what to do based on the file type
            """
            fileExtension = ""
            for i in range(len(self.__filename)-1,0,-1):
                if (self.__filename[i] == "."):
                    fileExtension = self.__filename[i:]
                    break
            try:
                return FILE_TYPES[fileExtension]
            except:
                return -1

    def write(self,dataToWrite):
        """
        Attemps to write to the file while handling exceptions such as TypeErros's and NameErrors
        """
        try:
            self.file.write(dataToWrite)
        except TypeError as typeError:
            pass
        except NameError as nameError:
            pass


    def read(self,bytesToRead = -1):
        """
        Attemps to read from the file while handling exceptions
        """
        try:
            self.file.read(bytesToRead)
        except Exception as e:
            pass


    def close(self):
        """
        Attemps to close the file handle while handling exceptions
        """
        try:
            self.file.close()
            self.closed = self.file.closed
        except Exception as e:
            pass
        
