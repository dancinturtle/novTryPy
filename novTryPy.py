##String Methods

x = 'small'
print x.capitalize()
## result = small

x = 'small'
print x.upper()
## result = small

x = 'SMALL'
print x.lower()
## result = small

x = "hello how are you doing today, are you ready?"
print x.count("are")
##result is 2

x = "This is a string!"
print x.find("a")
##result is 8

x = "where is the hello at" 
print x.index('hello')
##result is 13
x = [22,3,11,'hello','hello',22,'goodbye']
print x.index("hello")
##result is 3

x = 'this is gonna get split'
print x.split()
## result = ['this', 'is', 'gonna', 'get', 'split']

string = ["these","are","words","this is,","more"]
print ' '.join(string)
##Result is "these are words this is, more"

string = "we're gonna change this day, not this day"
print string.replace("day","month",1)
##Result is "we're gonna change this month, not this day"

string = "this addition to the string"
newstring = "Format used to create {thing}!".format(thing=string)

##List Methods
x = [1,3,4,5,6]
print len(x)
##Result is 5

x = [1,3,4,5,6]
print max(x)
##Result is 6

x = [1,3,4,5,6]
print min(x)
##Result is 1

x = [1,3,4,5,6]
print x.index(4)
##Result is 2

x = [1,3,4,5,6]
x.append(7)
print x
##Result is [1,3,4,5,6,7]

x = [1,3,4,5,6]
x.append(7)
x.pop()
print x
##Result is [1,3,4,5,6]

x = [1,3,4,5,6]
x.remove(4)
print x
##Result is [1,3,5,6]

x = [1,3,4,5,6]
x.insert(2,4)
print x
##Result is [1, 3, 4, 4, 5, 6]

x = [2,19,33,0,2,1,14]
x.sort()
print x
##Result is [0, 1, 2, 2, 14, 19, 33]

x = [4,5,6,7,8]
x.reverse()
print x
##Result is [8, 7, 6, 5, 4]

x = [4,5,6,7,8]
x.extend([9,10,11])
print x
##Result is [4, 5, 6, 7, 8, 9, 10, 11]


##Result is Format used to create this addition to the string!

#capitalize caps each word using

#upper puts all letters into upper case

#lower  puts all letters into lower case

#count number of reoocurances of an list item

#find returns the lowest instance occurance of the value, error code of -1

#index like find, but provided different error code ValueError

#split splits a string into a list

#join concatenates a list into one argument

#replace returns a copy of the string with occurances and replaces old value with new

#format acts like interpolation (string)

#len = returns the length of the object

#max returns the largest item in an interable or two or more arguments

#min returns smallest ""

#index provides index value, not list value

#append adds to the end of the target the value provided

#pop remove the value at the end of the target

#remove removes the first item of (x) from a list

#insert inserts variable to the position you provide

#sort sorts the items of the list in-place (low to high with no conditions)

#reverse reverses the elements in the list (in-place)

#extend extends the list with provided objects / new list