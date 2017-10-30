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
