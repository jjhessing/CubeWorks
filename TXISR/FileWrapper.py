
FILE_TYPES = {
    ".data" : 0,
    ".transmission" : 1,
}


class FileWrapper():
    """
    File Wrapper class to deal with file based exceptions and handling for primary use in the USU GASPACS Cubesat software. To open a file call the constructor FileWrapper(filename,mode,encoding)
    """


    def __new__(cls,filename,mode,encoding):

        def getFileType():
            """
            Takes in a filename which includes the file extensions and looks it up in a const dict of file types and returns an int for use in deciding what to do based on the file type
            """
            fileExtension = ""
            for i in range(len(filename)-1,0,-1):
                if (filename[i] == "."):
                    fileExtension = filename[i:]
                    break
            try:
                return FILE_TYPES[fileExtension]
            except:
                return -1



        try:
            #try to return a file object
            return open(filename,mode=mode,encoding=encoding)

        #catch all the exceptions 
        except FileNotFoundError as fileNotFound:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except FileExistsError as fileExists:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except OSError as osError:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        except Exception as exception:
            fileType = getFileType()
            #TODO:logic for handling based on file type
        finally:
            pass

        
