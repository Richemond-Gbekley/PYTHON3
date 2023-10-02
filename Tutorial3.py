#Tuples
#Tuples are used to store multiple items in a single variable
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1]
print("Tuples")
print("*******")
mytuple = ('Web developent ', 'Automation scripting' , 'Game Development' )
print(mytuple)

#Tuples are mostly like list , and since weve treated list , we wont do most of the things 
#But we would do what we dont know
#Some of the things we know already
#.Allowing Duplicate
#.List Length
#.Checking the type
#.List Constructors
#.Accessing List items
#.Negative indexing
#Looping


#Changing tuples values :NB: Since Tuples are not changeable, which means items cant be added, removed, or changed
#we need to change a tuple into list to be able to make a change in item , and back to the tuple
print("Changing Values of Tuples item")
print("*******************************")   #After we had changed the tuple into a list , we can now go ahead and change or add or remove an item.
mylist = list(mytuple)
print(mylist)
print("Changing , adding,and removing an item from list ")
print("************************************")
mylist[0] = 'Web scrapping'
mylist.remove('Automation scripting')
mylist.append("Networking")
print(mylist)
print("Changing it back to a tuple")
print("****************************")
mytuple = tuple(mylist)
print(mytuple)


#Unpacking in Python refers to the process of extracting values from a data structure 
# like a list, tuple, or dictionary, and assigning them to variables in a single statement.
# When you're working with tuples, you can use tuple unpacking to easily assign individual elements to separate variables.
print("\n")
print("Unpacking Tuples")
print("*****************")
mysecondTuple = ("Jammer" , "30$" , "To make signals unstable" , "Illegal", )
(Product ,Price ,  Usage , Status )= mysecondTuple
print(Product)
print(Usage)
print(Price)
print(Status)

#Using Asterisk
#You can also use the * operator to gather remaining elements into a single variable. 
#Since the number of item or values are more than the variable, id assign the rest to the 
#status and also its like the same data
print("\n")
print("Using Asterisk")
print("***************")
mysecondTuple = ("Jammer" , "30$" , "To make signals unstable" , "Illegal","Out of Stock", "New Model" )
(Product ,Price ,  Usage , *Status) = mysecondTuple
print(Product)
print(Usage)
print(Price)
print(Status)


#Set
#A set is a collection which is unordered, unchangeable*, and unindexed , Duplicates are not allowed
print("\n")
print("Set")
print("***")
myset ={'Zero day attack' ,'Social Engineering','Phishing'}
print(myset)

#Sets are mostly like list , and since weve treated list , we wont do most of the things 
#But we would do what we dont know
#Some of the things we know already
#.Allowing Duplicate
#.List Length
#.Checking the type
#.List Constructors
#.Accessing List items
#.Negative indexing
#Looping

#Join Two Sets
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another
print("\n")
print("Joining two Set")
print("****************")
myset2 ={'Sniffing','Back door','Enumeration','Phishing'}
myset3 =myset.union(myset2)
print(myset3)
print("\n")
         #OR
print("OR")
print("\n")
print("Joining two Set")
print("****************")
myset2 ={'Sniffing','Back door','Enumeration'}
myset.update(myset2)
print(myset)

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.print("OR")
print("\n")
print("Keep only the duplicates")
print("*************************")
myset4 ={'Sniffing','Back door','Enumeration'}
myset5 ={'Sniffing','Phishing','Enumeration'}
myset4.intersection_update(myset5)
print(myset4)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print("\n")
print("Keep all but not the duplicates")
print("*******************************")
myset4.symmetric_difference_update(myset5)
print(myset4)

print("\n")
         #OR
         #Return a set that contains all items from both sets, except items that are present in both:
print("OR")
print("\n")
print("This involves creating a new set")
print("*********************************")
myset6 = {'hey','alright','okay'}
myset7 ={'hey','not alright','okay'} 
myset8 = myset6.symmetric_difference(myset7)
print(myset8)


#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
mydict ={ "Name":"Dave",
         "Age" : "18",
         "Work Place":"Accra"}
print(mydict)

#Accessing Items in dictionary
#You can access the items of a dictionary by referring to its key name, inside square brackets:
print("\n")
print("Accessing items in Dictionary")
print("******************************")
print(mydict["Name"])

#There is also a method called get() that will give you the same result:
print("\n")
print("Accessing items in Dictionary")
print("******************************")
print(mydict.get("Age"))

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
print("\n")
print("Getting the list of all the return in the dictionary")
print("*****************************************************")
x = mydict.keys()
print(x)

#Get Values
#The values() method will return a list of all the values in the dictionary.
print("\n")
print("Getting the values")
print("*******************")
y = mydict.values()
print(y)
#Adding a new key and a value in the dictionary


print("\n")
print("Adding a anew key and value ")
print("****************************")
mydict['Address'] = "A341/9"
print(mydict)


#Get Items
#The items() method will return each item in a dictionary, as tuples in a list
print("\n")
print("Getting the list of items ")
print("**************************")
z=mydict.items()
print(z)


#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().


print("\n")
print("Copying dict ")
print("**************")
mydict1 = mydict.copy()
print(mydict1)

#if -else and key words in python3
#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.

#keywords
#and
#or
#not


#Using the if condition
print("\n")
print("Using the if condition ")
print("************************")
password ="1234"
username ="Ken"

user_password =input("Enter Password \n")
user_username = input("Enter Username \n")

if user_password == password  and user_username == username :
  print("Successfully Logged in")  
else :
    print("Access denied , wrong credentials")
    
    #Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
print("\n")
print("Using the Elif condition ")
print("*************************")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
# The while loop
#Python has two primitive loop commands:
#while loops
#for loops
print("\n")
print("While condition ")
print("****************")
count = 0
while count <=5 :
    print(count)
    count += 1

print("\n")
print("While condition  with break")
print("****************")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
print("\n")
print("While condition  with continue")
print("********************************")
i = 0
while i <= 6 :
    i += 1
    if i == 3 :
        continue
    print(i)
    
    print("\n")
print("While condition  with else")
print("***************************")
count = 0
while count <=5 :
    print(count)
    count += 1
else:
    print("i is exausted")
    
    
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

    print("\n")
print("Foor Loop")
print("***********")
for x in mydict :
    print(x)
    
    print("\n")
print("For Loop with break")
print("**********************")
for x in mydict :
    print(x)
    if x == "Age" :
        break
        
        
   # print("\n")
print("For Loop with break")
print("**********************")
for x in mydict :
    
    if x == "Age" :
        break
    print(x)
    
    print("For Loop with continue")
print("****************************")
for x in mydict :
    
    if x == "Age" :
        continue
    print(x)
        