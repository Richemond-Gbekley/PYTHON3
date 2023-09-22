#Escaping Characters in Strings
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quote
print("ESCAPE CHARACTERS")
print("*****************")
txt = " Zeroday Attack \" said by Hackathon\" is possible "
print (txt)

# https://www.w3schools.com/python/python_strings_methods.asp (Link to the types of method used in strings and their description)

#Boolean Values
print("Boolean Values")
print("**************")
print(10 > 4) #Prints true or false depending on the condition
print (4 < 4) #Prints true or false depending on the condition
print("\n")

a = 10
b = 20
if a > b:
    print("a is greater than b")
    
else:  print("b is greater than a")
print("\n")
#List
#Lists are used to store multiple items in a single variable.
#Can be applied for all kinds of data types and can contain different datatype
print("List")
print("*****")
mylist = ["Ethical Hacking","Pentesting","Data Science","Artificial INtelligence"]
print(mylist)
#List items are ordered, changeable, and allow duplicate values.

#Allowing Duplicates
mylist = ["Ethical Hacking","Pentesting","Data Science","Artificial INtelligence","Data Science"]
print(mylist)
print("Data science has been duplicated")

#List Lenght
print("\n")
print("List Lenght")
print("************") #To determine the lentgh of the list
print (len(mylist)) # It prints out the number of list available


print("\n")
print("Type")
print("*****")

#Checking the Type 
#Its noted that to check the type , you use the syntax type 
print(type(mylist))

print("\n")
print("List()")
print("*******")

#List Constructor list()
mylist1 = (("Ethical Hacking","Pentesting","Data Science"))
print(mylist1)

#Accessing List Items
#This motive is achieved with the help of using indexing
print("\n")
print("Accessing List")
print("****************")
print(mylist1)
print("Printing the thrid value ::: " + str(mylist1[2]))


#Negative indexing
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item and so on.
print("\n")
print("Neagtive indexing")
print("****************")
print(mylist1)
print("Printing the first value ::: " + str(mylist1[-3]))

#Range of indexing

print("\n")
print("Range of indexing")
print("****************")
print(mylist1)
print("Printing from the first value , index 0 (included) to the last value (excluded) ::: " + str(mylist1[0:2]))

#Checking if the item exists

print("\n")
print("Checking if the item exists")
print("****************************")

if "Data Science" in mylist1: #This is case sensitive
  print("yes , i see it")    
else :
    print("Access denied because i dont see it ")
    

if "Data science" in mylist1: #This is case sensitive
  print("yes , i see it")    
else :
    print("Access denied, because i dont see it ") #This prints out access denied because i dont see it 
                                                  #because of the fact the the scince started with an ups S
  
  #Change item value
  #To change the value of a specific item, refer to the index number
print("\n")
print("Changing item value")
print("********************")
mylist[2] = "Web Testing"
print(mylist)

#Change a range of item values
print("\n")
print("Changing item value")
print("********************")
mylist[1 : 2] = "Web Testing" , "Cryptography"
print(mylist)
    
     
#Insert new item
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
print("\n")
print("Insert new item")
print("********************")
mylist.insert(6 , "Forensics")
print (mylist)

#Append new item
#To add an item to the end of the list, use the append() method:
print("\n")
print("Append new item")
print("****************")
mylist.append("web exploitation")
print(mylist)   #difference between append and insert is, append would add to the last item
                #without having to soecify the index, where as insert would add an item to the 
                #specific index specified
                
#Extending a new list
#To append elements from another list to the current list, use the  extend() method:
print("\n")
print("Append new item")
print("****************")
mylist2 = ["Java", "C++" ,"Javascript" ,"sql"]
mylist.extend(mylist2)
print(mylist)
                
