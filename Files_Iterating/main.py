
from Requesting_File_Names import Requesting_Files_Names
import os
## this is to get the current directory name
dir = os.path.dirname(__file__)
## this is to get the folder of all the pictures. TODO : We will need to change it depending on where we put the pictures
FolderName = os.path.join(dir,'/test_images_8_bit')


request = Requesting_Files_Names(dir,FolderName)

request.run() 
