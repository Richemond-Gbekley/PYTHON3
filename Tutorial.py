#Variable 
#Variables: In Python 3, variables are created by assigning a value to 
#a name. Eg  x =5 , creates a variable called x and assigns the value  5 

#Many values to many variables
x = "5"
print ( "one Values to one variable ::: " +x) # this prints out 5 , as 5 was assigned to x
print("******************************") 
#Many values to many variables
x,y,z = "Hackthon","is","Real"
print("Many Values to Many variable ::: " +x,y,z)
print("*********************************")
#Datatype
# Datatype : In python 3 , supports several built -data ttpes
#including integers, float,string, dictionaries etc
name = str ("Hackathon")
print("Datatype string ::: " +name) # this prints out hackathon as hackathon which is an string is assigned to the variable name 
print("************")
#Operators
#Operators : In pyhthon 3, supports a variety of operators (+-*), 
#comparison operators , including arithmetic operators (<>==!) or logical
#operators (and ,or not )
add = 5 + 20 
answer = add 
print("Operators ::: " +str (answer) ) # as the addition was assigned to the  varaible add, we again assigned
print("*************")#the answer to the varible answer and printed out the answer using the declared variable
               #NB::: Convert the integer to a string before concatenating(STR)(Text type)
               
          #Pulling out , from a list     
Likes = ["Hack" , "Pen Test" ," Web Test"]
x,y,z = Likes
print("I pulled out the firts like ::: " +x)
print("*******************************")
print("I pulled out the last like ::: " +z)
print("*******************************")

#GLOBAL AND LOCAL VARIABLES
print("GLOBAL AND LOCAL VARIABLES")
print("***************************")

#Global Variables
#Are created outside a function and can be accessed by everyone.
print("GLOBAL VARIABLES")
print("*****************")
a = "My World"

def Ethicak_Hacking():          #Since a was made a global variable is was able to be accessed outside the fuction
  print("Python is " + a)

Ethicak_Hacking()
print("\n")

#Local Variables
#Only accessed inside a function
print("LOCAL VARIABLES")
print("****************")
s = "Blue team"
def Pen_testor():
    s = "Red Team"                  #Noticing that there are the same variable s, our output was not conflicted by the same variable
    print("im part of " + s)        #since one was a local variable and another was a global variable
    
Pen_testor()
print("Im part of " +s)
print("\n")
print("Data types")
print("***********") # Determing the type of datatype is helped by calling the command line type
year = 2001
print("2001 is the datatype::: " + str(type(year)))
print("***********************")
 

#RANDOM NUMBERS
print("\n")
print("RANDOM NUMBERS")    # python uses an in built module for producing random numbers which is random
print("***************")
import random
print("printing random number from between 1 to 10  \n"+ str( random.randrange(1,10)))

#Printing Multiple strings : is done with the help of 3 quotes
print("\n")
print("Printing multiple strings")
print("***************************")
Documentation = """So im submitting a report on the pen test 
i did , so keep silence , head straight, take your coffee , 
and read so that you can get everything im saying , innit"""
print(Documentation)

#Arrays are arrays
print("\n")
print("String are arrays")
print("*******************")
b = "I love Hacking"
print("printing the letter l :::", b[2])

#Looping through arrays
print("\n")
print("looping through arrays")
print("*******************")       #looping would go through and print whatever its looping through , till it gets to the number of 
                                   #letters found in the sentence , as i love hacking was printed 14 times while looping
for x in "I love Hacking" :
    print(b)
    
    #String Length
print("\n")
print("String Length")         # uses the built module len , to print out the 
print("*******************")
print(len(b))
    
    #Checking for strings
print("\n")
print("Check for strings")         # would print out true , if the word exists in the specified variable 
print("*******************")       #and false if it doesnt exist
print("love" in b)
print("hate" in b)  
print("hate" not in b)
print("love" not in b)

    #if statement
print("\n")
print("if statement")         #  
print("*************")
if "love" in b:
    print("yes, i found it")
else:
 print("youve got to look elsewhere")
 
 
if "hate" in b:
  print("yes, i found it")
else:
    print("youve got to look elsewhere")
    
    
 
     #Slicing strings : Printing specific range in a variable
print("\n")
print("Slicing string")         
print("*************")
print(b[2:6])
print(b[:6])  #Leaving out the first index, would start from the begining
print(b[1:]) #Leaving out the second index would finih till the last

#String Format: combining strings and numbers. The format() method takes the passed arguments
# formats them, and places them in the string where the placeholders {} are
print("\n")
print("String Format")         
print("*************")
number = 200
txt = " When you see the number {} it means okay, and that you are good to go"
print(txt.format(number))
# for multiple formatting :NB you can use indexing to help arrange it in the order in which you want
print("\n")
print("Multiple string Format")         
print("************************")
number = 200
command = "select"
tool = "sql_injection"

Hacking = " i tried web testing , and i used {2} with the payload command {1} and i got {0} which means ok"
print(Hacking.format(number,command,tool))

