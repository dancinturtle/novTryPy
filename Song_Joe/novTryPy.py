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