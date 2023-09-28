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
       #                 ***********

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
                
#Removing an item from a new list
#The remove() method removes the specified item.
print("\n")
print("Remove item")
print("************")
mylist.remove("Java")
print(mylist)


#Pop
#The pop() method removes the specified index.
print("\n")
print("Pop item")
print("************")
mylist.pop(8)
print(mylist)

#del will remove the specific index
#del would also delete the list 
#Eg del <list>
#clear , would clear the list 

#loop through a list
print("\n")
print("Loop through the list")
print("**********************")
for x in mylist :
    print(mylist)
    
    #Loop through the index numbers
    #Use the range() and len() functions to create a suitable iterable.
    for i in range(len(mylist)):
        print(mylist[i])
        
        #Using a while loop
        #Use the len() function to determine the length of the list, then start at 0 
        # and loop your way through the list items by referring to their indexes.
       # i = 1
        #while i < len(mylist) :
         #   print(mylist[i])
          #  i + 1
            
            
           # Looping using list comprehension
           #List Comprehension offers the shortest syntax for looping through lists:
print("\n")
print("Looping using the list comprehension")
print("*************************************")
[print(x) for x in mylist]

            #List Comprehension
            
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fields, you want a new list, containing only the fields with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

print("\n")
print("list comprehension_FOR STATEMENT") #You first need to create your empty list or new list
print("**********************************")#Easy way : Since i have created my new list(mylist3) , for all the elements(x) in 
mylist3 = []                               #(mylist) , if there is an 'a' in the elements in (mylist) , then (append), ie add all those 
for x in mylist:                          #elements in the newlist (mylist)
  if "a" in x:
    mylist3.append(x)

print(mylist3)
print(mylist) # We would see the fields that were taken from mylist and placed in mylist3 to create a new list
#Note this is the For statement not list comprehension
print("This result is not list comprehension rather FOR STATEMENT")

print("\n")
print("list comprehension") 
print("********************")

#With List comprehension, you can do this in a single line of code.
mylist4 = [x for x in mylist if 'a' in x]   #Easy way : Creating the new list (mylist4), fill the list with elements(x)
print(mylist4)                            #but ,first go through the elements in (mylist) , now if there is an 'a' in (mylist)(x) , then 
print(mylist)                             #fill (mylist4) with those elements.
                                    #NB:newlist = [expression for item in iterable if condition == True]
                                    
                  #Condition
#The condition is like a filter that only accepts the items that valuate to True
#The condition if x != "Ethical Hacking"  will return True for all elements other than "Ethical Hacking", making the new list
# contain all fruits except "Ethical Hacking".
print("\n")
print("!=")
print("****")
mylist4 = [x for x in mylist if x != "Ethical Hacking"]
print(mylist4)   # Ethical Hacking would be excluded
print(mylist) 

print("\n")
print("without the if")   #Without the if
print("***************")
mylist4 = [x for x in mylist]
print(mylist4)   #This would be like copy one list to another

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
print("\n")
print("Iterable")   
print("*********")
mylist4 = [x for x in range(10)]
print(mylist4)

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
print("\n")
print("Iterable")   
print("*********")
mylist4 = [x for x in range(10) if x < 9]
print(mylist4)


#Sort
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#this means its would be arranged from uppercase to lowercase.
#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function : This would deactivate the case sensitive nature of the programme
print("\n")
print("Sort")   
print("****")
mylist.sort()
print(mylist)

print("\n")
print("Sort Descending")   
print("*****************")
#Sort Descending
#To sort descending, use the keyword argument reverse = True:
mylist.sort(reverse=True)
print(mylist)

print("\n")
print("Customize sort function")   
print("*************************")
#Customize , sort function
#You can also customize your own function by using the keyword argument key = function

def myfunc(n):
  return abs(n - 50)

numberlist = [100, 50, 65, 82, 23]
numberlist.sort(key = myfunc)
print(numberlist)

print("\n")
print("Making it not case sensitive")   
print("******************************")
mylist.sort(key= str.lower)
print(mylist)


#Reverse order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements
print("\n")
print("Reverse order")   
print("**************")
mylist.reverse()
print(mylist)
