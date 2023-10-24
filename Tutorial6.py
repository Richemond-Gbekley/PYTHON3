#file handling 
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists


# In addition you can specify if the file should be handled as binary or text mode

#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#file = open("Myfile.txt" ,"x")
#file = open("Myfile.txt","rt")
#f = open("C:/Users/riche/IdeaProjects/BS456102720/Data/ results.txt" ,"rt")
#myfile1 = open("Readme.txt" , "r")
#print(myfile1.read())

#read only part of the file 
#print(myfile1.read(1))
#myfile1.close()



#Create , read, write and close

#myfile1 = open("Readme.txt" , "a")
#myfile1.write("\n Im here to spy")
#myfile1.close

#myfile1 = open("Readme.txt", "r")
#print(myfile1.read())


#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function:
#import os 
#os.remove("Myfile.txt") 

#import os 
#if os.path.exists ("Myfile.txt") :
 #   os.remove("Myfile.txt")
#else :
 #   print("File does not exist")
    
    
    #Delete Folder
#To delete an entire folder, use the os.rmdir() method:
import os 

try:
    if os.path.exists("M.txt"):
        os.remove("M.txt")
    else:
        raise FileNotFoundError("File does not exist.")
except FileNotFoundError as e:
    print(e)

    

