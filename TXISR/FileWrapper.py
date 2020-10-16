
FILE_TYPES = {
    ".data" : 0,
    ".transmission" : 1,
}


class FileWrapper():
    """
    File Wrapper class to deal with file based exceptions and handling for primary use in the USU GASPACS Cubesat software. To open a file call the constructor FileWrapper(filename,mode,encoding)
    """


    def __init__(self,filename,mode,encoding):
        self.__filename = filename
        self.__mode = mode
        self.__encoding = encoding
        self.__file = self.openFile(self.__filename,self.__mode,self.__encoding)


    def __openFile(self):
        try:
            #try to return a file object
            return open(self.__filename,mode=self.__mode,encoding=self.__encoding)

        #catch all the exceptions 
        except FileNotFoundError as fileNotFound:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except FileExistsError as fileExists:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except OSError as osError:
            print("shitt")
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except Exception as exception:
            print("shitt")
            fileType = getFileType()
            #TODO:logic for handling based on file type
        finally:
            pass


    def getFileType(self):
            """
            Takes in a filename which includes the file extensions and looks it up in a const dict of file types and returns an int for use in deciding what to do based on the file type
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

    def write(self,message):
        try:
            self.__file.write(message)
        except TypeError as typeError:
            pass
        except NameError as nameError:
            pass


    def read(self,bytesToRead = -1):
        try:
            self.__file.read(bytesToRead)
        except Exception as e:
            pass


        
