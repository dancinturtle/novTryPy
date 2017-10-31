# To iterate through each element in a list, use the "for-in" loop. The variable defined is the placeholder for each value.
# The following will print each name in the "characters" list
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
for person in characters:
    print person


#Include the following 'String' methods:
#################################################################################################
#If the following is a string:
str="This is a String Example.....Ha!";

# The following method returns a copy of the String with _ONLY_ its 1st (first) character capitalized. 
#(The print commande prints it to python cmd / bash.)
print "str.capitalize() : ", str.capitalize()

# The following two methods (.upper() and .lower()) convert all of the characters in a string data type to UPPERCASE and to lowercase.
str.upper()
str.lower()

#The .count() method adds up the number of times a character or even as sequence of characters appears in a string data type.
str.count("t") #This will return 2.

#The .find() method will search for a specific character or characters in a string data type. 
#NOTE: The method resembles between a Capitalized and a lower case character.
#The result is the position in a string at which the sequence of characters begins.
str.find("i") 
2
str.find("is")
5
#To look for the 2nd occurence of a specific character in a string, specify a range. The following will start to look for the "i" 
#character at the 5th position:
str.find("i", 5)
5 #Coincidentally, the "i" is also at the 5th position in the specified string.
#Like slicing, we can do tell .find() to search backwards: .find(str or char, beg=0, end=len(string)).
str.find("a", 10, -2) 
19

#Python Strings are Lists of characters. Each is given an Index from 0 (at the beginning) to the length (String.len()) minus one
# (at the end).
#Python supports negative indexes. To count from the end of a String, start at -1 (not a 0).
#The .index() method determines if a subtring (String) occurs in String data type.
str1 = "this is string example...wow!!!";
str2 = "exam";
print str1.index(str2); 
#prints out:
15
#As with .find() method, .index() can have a range by specifiying the starting index ('beg' is 0 by default) and an ending index
# ('end' is len(string) by default):    str.index(sub, beg = 0 end=len(string)).
#An .index() method raises an Exception error if the substring is not found.

#A .split() method is frequently used to break a large string down into smaller chunks, or smaller strings.
x='blue,red,green'
x.split(",")
# The rusult will be:
[‘blue’, ‘red’, ‘green’]
a, b, c = x.split(",")
# Will assign each of a, b, and c it's smaller chunk of the original 'blue, red, green' string:
a
'blue'

b
'red'

c
'green'

#2nd Example:
words = "This is random text we'regoing to split apart"
words2 = words1.split(" ")
print words2 ##(or just type >>>words at conmand prompt)
['This', 'is', 'random', 'text', 'we're', 'going', 'to', 'split', 'apart']

# The .join() method returns a String in which the String elements of sequence have been joined by 'str' separator: 
# str.join(sequence)
#Example(s):
s="-";
seq= ("a", "b", "c"); #This is sequence of strings.
print s.join(seq)
#Prints out:
a-b-c

# The .replace() method returns a copy of a string in which the occurences of 'old' have been replaced with 'new', 
#optionally restricting the number of replacements to 'max': str.replace(old, new[, max])
str = "this is string example....wow!!! This is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)
#The above two print statements will print out:
thwas was string example....wow!!! Thwas was really string
thwas was string example....wow!!! Thwas is really string


#The .format() method is an extremely convenient way to format text exactly the way you want it: template.format(p^0, p^1, ..., k^0=v^0, k^1=k^1, ...):
>>>"The {structure} sank {0} times in {1} years.".format(3, 2, structure='castle')
#Will return:
'The castle sank 3 times in 2 years.'
#When you need to include the actual "{" and "}" characters in the result, double them, like this:
>>> "There are {0} members in set {{a}}.".format(15)
'There are 15 members in set {a}.'


#Include the following 'List' methods:
#########################################################################
# The .len() method returns the number of elements in the list: len(list)
#EXAMPLE:
list1, list2 = [123, 'xyz', 'zara'], [456,'abc']
print "First list length : ", len(list1)
print "Second list lenth : ", len(list2)
# Above 2 print statements will print:
First list length : 3
Second list length : 2

#The .max() method returns the elements from the list with maximum value: max(list)
# Assuming the above 2 lists:
list2 = [456, 700, 200]

print "Max value element : ", max(list1)
print "Max value element : ", max(list2)
# The printed results:
Max value element : zara
Max value element : 700

#The .min() method returns the elements from the list with mininum value.
#If utilizing the same examples as for the .max() method above, the returned .min() values of the both lists are:
#list1:
123
#list2 (list2=[456, 700, 200)]:
200

#The .index() method returns the lowest index in the list that 'obj' appears: list.index(obj)
#EXAMPLES:

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
print "Index for xyz : ", aList.index ( 'xyz' )
print "Index for xyz : ", aList.index ( 'zara' )
#PRINTS OUT:
Index for xyz : 1
Index for zara : 2

#The method .append() appends a passed 'obj' into the existing list: list.append(obj)
#The method does NOT return any value.
#EXAMPLES:
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList
#PRINTS OUT:
Updated List : [123, 'xyz', 'zara', 'abc', 2009]

#The .pop() method removes and returns the last or the requested object or 'obj' from the end of the list: list.pop(obj = list[-1])
#EXAMPLES:
#Using the same example aList as above:
print "A List : ", aList.pop()
print "B List : ", aList.pop(2)
#PRINTS OUT:
A List : abc
B List : zara

#The .remove() method DOES NOT return any value, but it removes the given object from the beginning of the list, starting at 
# index = 0 (as opposed to the .pop() method).
#The method does NOT return any value.
#EXAMPLES:
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('xyz');
print "List : ", aList
#Prints out:
List : [123, 'zara', 'abc', 'xyz']


#The .insert() method inserts object 'obj' into list at offset 'index': list.insert(index, obj)
#The method does NOT returm any value: list.insert(index, obj)
#EXAMPLES: 
aList = [123, 'xyz', 'zara', 'abc'];
aList.insert(3, 2009)
print "Final result : ", aList
#PRINTS OUT:
Final List : [123, 'xyz', 'zara', 2009, 'abc']

#The .sort() method sorts objects of a list, using compare 'func', if given: list.sort([func])
#The method does NOT return any value.
#EXAMPLES:
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.sort();
print "List : ", aList
#PRINTS OUT:
List : [123, 'abc', 'xyz', 'xyz', 'zara']
#INCLUDE EXAMPLE OF A compare 'func'...........!!!

#The .reverse() method reverses objects of list in place: list.reverse()
#The method does NOT return any value.
#EXAMPLES:
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print "List : ", aList
#PRINTS OUT:
List : ['xyz', 'abc', 'zara', 'xyz', 123]

# The .extend() method APPENDS the contents of 'seq' to list: list.extend(seq)
# The method does NOT return any value.
#EXAMPLES:
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList
#PRINTS OUT:
Extended List : [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
