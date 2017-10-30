#Functions

#Capitalize first letter of string
def capitalize(str):
    return str.capitalize()

#Capitalize the whole string
def upper(str):
    return str.upper()

#Lowercase the whole string
def lower(str):
    return str.lower()

#count gets the number of occurrences of substring in the range.
#Returns true if found, false if not found
#str.count(substring, start, end)
def count(str, sub):
    return str.count(sub)

#find finds substring in string
#str.find(sub,start,end)
def find(str, sub):
    return str.find(sub)

#index same as find, but raises an exception if not found
def index(str, sub):
    return str.index(str, sub)

#Function calls
str = "hello"
print capitalize(str)
print upper(str)
print lower(upper(str))
print count("asdfqwerasdfqwerasdf", "qwer")
print find("codingdojo","ing")