#Enter Python code here and hit the Run button.

print("Hello world")

# name=input("What is your name?")
# age = int(input("What is your age??"))


# print("Hello "+ name)  # Concatenate
# print(type(age))  # type method to return datatype


# first_number = input("Enter first number")
# second_number = input("Enter Second number")

# concat=(first_number + second_number)
# sum=int(first_number)+int(second_number)

# print(concat)
# print(sum)
# print("Sum is " +str(sum))  # Converted int into string for concatenation

# print(name.upper())  #Upper Case
# print(name.lower())  #Lower Case
# print(name.title())  #Proper Case

# print(name[0]) # Print character e.g. Rakesh - R
# print(name[0:4]) # Print character e.g. Rakesh - Rake


# for character in name:
#     print(character)     # Print Each character in each row

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']


# b="rakesh"
# print(b[-4:-2])

# print("my name is " + name)

mylist=["apple", "banana", "cherry","grapes","watermelon"]
mymylist=["kiwi", "mango","papaya","guava"]


list1=["Ram","Sham","Seeta","Geeta"]
list2=[40,10,20,60,30,50]
list3=[True,False,True,False]

the_list=list(("mobile","watch","Airpods","bottle"))



print(mylist)

# print(len(mylist))  # Length of the List
# print(type(list1))  # Type
# print(type(list2))  # Type
# # print(type(list3))  # Type
# print(the_list)     # List Contrustor

# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:6])     # Range
# print(mylist[:6])     # Range By leaving out the start value
# print(mylist[2:])     # Range By leaving out the end value
# print(mylist[-5:-2])  # Range by using Negative Indexes


# if "banana" in mylist:              ##### Finding the item in the list 
#     print("Yes, banana is on the list")


# mylist[1]="Orange"         ### Changing the item value
# mylist[3:5]=["lemon","pineapple"]             ##### Changing the item in range
mylist.insert(3,"muskmelon")            ####### Inserting Item
mylist.append("cherry")          ######### Append Items
mylist.extend(mymylist)            ########## Extending the list

# mylist.remove("Orange")          ###### Removing Specific Item
# mylist.pop(4)                    ###### Removes the specified index, if do not specify the index, the method removes the last item.
# del mylist[1]            ####### Deletes one specified index, if it is not specified then del the whole list
# mylist.clear()             ###### Clears the list but not delete the list.


# ##### For Loop for the list #####

# for i in mylist:
#     print(i)


# for i in range(len(mylist)):
#     print(mylist[i])

# ########## While Loop #######

# i=0
# while i < len(mylist):
#     print(mylist[i])
#     i=i+1


# [print(x) for x in  mylist]  ###### For shortcut ######


######## making a new list and add in data from previous list ###
# newlist=[]

# for x in mylist:
#     if "a" in x:
#         newlist.append(x)

# newlist1=[x for x in mylist if "a" in x]       ##### shortcut for above

# newlist=[x for x in mylist]    ######## SHORTCUT for copying a list

# newlist=[x for x in range(5)]     ########## returning in range of 0 - 4

# newlist=[ x for x in range(10) if x < 7]    ########## returning values which are less then 7 in range of 0 - 10

# newlist=[x.upper() for x in mylist]    ########### Upper case using for loop option

# newlist=["hello" for x in mylist]       #########  replacing the value in mylist to hello

newlist=[x if x != "banana" else "cherry" for x in mylist]     ############ Return "Cherry" instead of "banana"

# newlist.sort()          ######### Sort the list alphabetically
newlist.sort(reverse= True)

########### Created function close to 4 ######
def myfunc(n):
    return abs(n-4)

list2.sort(key=myfunc)     ######  sort by function

list2.reverse()              ###### reverse the order.
# list4= list2.copy()        ###### Coping the list using copy method.
# list4 = list(list3)        ###### Coping the list using List method.
# list4 = list3 + list2        ###### Joining two list in one list.

# list3.extend(list2)            ####### Use the extend() method to add list2 at the end of list3


print(list2)
print(list3)

# print(mylist)
# print(newlist)
# print(newlist1)





