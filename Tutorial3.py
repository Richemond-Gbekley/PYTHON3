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

