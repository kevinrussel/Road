import os
import time
import threading

# reset the final output.txt file
with open("output.txt", "w") as file:
    file.write("")  # this clears the file

## ok so what I can do right now is to make a class
## this will get us the the current path of the file.
# and I want to do is to to make a class and a main class..

class Requesting_Files_Names:
    ## we want to make a constructor that creates an object that has the directory namee and so forth.
    
    def __init__(self,currentFilePath,pictureDirectoryName):
        self.currentFilePath = currentFilePath
        self.pictureDirectoryName = pictureDirectoryName

        self.filename = os.path.join(currentFilePath, 'test_images_8_bit')
        print(self.filename)
        self.checkThreading = False



    def fun1(self):
        print("Hello there!")
        time.sleep(0.0025)


    def run(self):
        while self.checkThreading == False:
            for name in os.listdir(self.filename):
                with open(os.path.join(self.filename,name)) as f:
                    threading.Thread(target=self.fun1).start()
            self.checkThreading = True



