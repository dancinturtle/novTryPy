#String Methods

print "Capitalize first letter of string"
#var.capitalize()
str = "hello world"
print str.capitalize()

print "Capitalize the whole string"
#var.upper()
str = "hello"
print str.upper()

print "Lowercase the whole string"
# var.lower()
str = "HELLO"
print str.lower()

print "count gets the number of occurrences of substring in the range."
#Returns true if found, false if not found
#str.count(substring, start, end)
str = "hello goodbye hello bye"
print str.count("bye",0,len(str))

print "find finds substring in string"
#str.find(sub,start,end)
str = "hi bye hey cya hello goodbye"
print str.find("cya", 0, len(str))

print "index is same as find, but raises an exception if not found"
#str.index(sub,start,end)
str = "hi bye hey cya hello goodbye"
print str.index("hello", 0, len(str))

print "Splits string according to delimiter str"
#str.split(str, num)
#str where it splits. if empty, then looks for space
#num: number of lines minus one
str = "hello hi hey hola"
print str.split()

print "Joins elements with sequence"
#str.join(sequence)
#sequence: joined by string sequence
str = ["hi", "bye", "hey", "cya"]
seq = "-"
print seq.join(str)

print "Replaces old string with new "
#str.replace(old,new,num)
#num: occurrences.(optional, default=1)
str= "hello hi hey bye"
print str.replace("bye","hola")

print "Format allows variables to concatenate in string"
#print ("hello {} {} hi" .format("hey","bye"))
str = "hello hi {} hey"
print (str.format("hola"))

#List Methods

sequence.len()
#returns length of a sequence
print len(characters)
#prints 5

sequence.upper()
#returns the upper case version of the string object calling .upper()
# not in place
print ‘abc’.upper()
#ABC

max(arr)
#returns max of a sequence:
arr=[2,5,7,2,10]
max(arr)
#returns 10

min(arr)
#opposite of max

arr.index(value)
#returns index of a value
arr=[2,5,7,2,10]
arr.index(5)
#returns 1

arr.append(value)
#appends a value to a list
arr=[2,5,7,2,10]
arr.append(3)
#arr becomes [2,5,7,2,10,3]

arr.pop(index)
#removes arr[index] from arr, and returns the removed value
arr=[2,5,7,2,10]
arr.pop(3)
#arr becomes [2,5,7,10], returns 2

arr.remove(value)
#removes the first matching value in arr
arr=[2,5,7,2,10,3,6,10]
arr.remove(10)
#arr becomes [2,5,7,2,3,6,10]

arr.insert(index, value)
#inserts value at arr[index]; if index=len(x) then it’s the same as x.append(value)
arr=[2,5,7,2,10]
arr.insert(0,’bonus’)
#arr becomes [‘bonus’,2,5,7,2,10]

arr.sort()
#sorts arr in place
#the same as sorted(arr)
arr=[2,5,7,2,10]
arr.sort()
#arr becomes [2,2,5,7,10]

arr.reverse()
#reverses arr
arr=[2,5,7,2,10]
arr.reverse()
#arr becomes [10,2,7,5,2]

arr1.extend(arr2)
#concatnates arr2 to the end of arr1, in place of arr1
arr1=[2,5,7,2,10]
arr2=['bad','muther']
arr1.extend(arr2)
#arr1 becomes 
[2, 5, 7, 2, 10, 'bad', 'muther']

