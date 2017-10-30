# Include the following string methods:

# capitalize
# upper
# lower
# count
# find
# index
# split
# join
# replace
# format

#.capitalize()
#converts all of the characters to uppercase
#example below
str = "franklin" 
str.capitalize()#Franklin


#.upper() 
#converts all of the characters to uppercase
#example below
str = "franklin" 
str.capitalize()#Franklin

#.count()
#this method adds up the number of tiimes a character or sequence of characters appears in a string
#example below
s = "That that is is that that is not is not that it it is" 
s.count(t)#13


#.find()
# this method searches for a specific character or characters in a string.
#example below
s = "on the other hand, you have different fingers"
s.find("hand")#13

#.replace()
#string.replace(str, old, new[, maxreplace])
#Return a copy of string str with all occurrences of substring old replaced by new. If the optional argument maxreplace is given, the first maxreplace occurrences are replaced.
myTakeAway = 'Amy said python is easy to learn' 
myConclusion = myTakeAway.replace('easy', 'hard')
print(myConclusion)#Amy said python is hard to learn

#.index()
#str.index(sub[, start[, end]])
#Like find(), but raise ValueError when the substring is not found.
myTakeAway = 'Amy said python is easy to learn' 
myTakeAway.index(20)#TypeError: expected a character buffer object

#.split()
#The method split() returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
#
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )
"""When we run above program, it produces following result −

['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']"""


#join()
#The method join() returns a string in which the string elements of sequence have been joined by str separator.
#example
s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )#a-b-c

#format()


print "My name is %s and weight is %d kg!" % ('Zara', 21)
#When the above code is executed, it produces the following result −
#My name is Zara and weight is 21 kg!

# Include the following list methods:
# len
# max
# min
# index
# append
# pop
# remove
# insert
# sort
# reverse
# extend

#.len()
# The method len() returns the number of elements in the list.
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print "First list length : ", len(list1)#3
print "Second list length : ", len(list2)#2

# .max()
#The method max() returns the largest of its arguments: the value closest to positive infinity.
print max(80, 100, 1000) : # 1000

#min()
#The method min() returns the smallest of its arguments: the value closest to negative infinity.
print "min(80, 100, 1000) : ", min(80, 100, 1000)  #80

#.index()
#The method index() returns the lowest index in list that obj appears.

aList = [123, 'xyz', 'zara', 'abc'];
print "Index for xyz : ", aList.index( 'xyz' ) #1

#.append()
#The method append() appends a passed obj into the existing list.
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );#Updated List :  [123, 'xyz', 'zara', 'abc', 2009]


#.pop()
# The method pop() removes and returns last object or obj from the list.

aList = [123, 'xyz', 'zara', 'abc'];
print "A List : ", aList.pop()
print "B List : ", aList.pop(2)
#When we run above program, it produces following result −

A List :  abc
B List :  zara


#.remove()
# obj − This is the object to be removed from the list.
# Return Value
# This method does not return any value but removes the given object from the list.
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('xyz');
print "List : ", aList
aList.remove('abc');
print "List : ", aList
# When we run above program, it produces following result −

List :  [123, 'zara', 'abc', 'xyz']
List :  [123, 'zara', 'xyz']

#.insert()
# The method insert() inserts object obj into list at offset index.
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print "Final List : ", aList
# When we run above program, it produces following result −

Final List : [123, 'xyz', 'zara', 2009, 'abc']

#.sort()
#The method sort() sorts objects of list, use compare func if given.
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.sort();
print "List : ", aList
# When we run above program, it produces following result −

List :  [123, 'abc', 'xyz', 'xyz', 'zara']

#.reverse()

# The method reverse() reverses objects of list in place.

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print "List : ", aList
# When we run above program, it produces following result −

List :  ['xyz', 'abc', 'zara', 'xyz', 123]

#extend()
# The method extend() appends the contents of seq to list.  
# Following is the syntax for extend() method −
# list.extend(seq) 


aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList 
# When we run above program, it produces following result −

Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']