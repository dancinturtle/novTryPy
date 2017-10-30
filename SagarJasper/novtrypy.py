#Capitalizes the first character in the string
name = "asasgsasr"
print name.capitalize()

#makes all characters in the string uppercase
print name.upper()

#makes all characters in the string lowercase
print name.lower()

#looks for given substring in the string and returns how many times it occurs
#also takes optional parameters that gives range to search in
print name.count("a")
print name.count("a", 0, 2)

#finds given substring in string and returns index it is located in
#also takes optional parameters that gives range to search in
print name.find("g")
print name.find("s", 0, 2)

#returns lowest index of given element in string
print name.index("r")
print name.index("s")

#splits up string based on given first parameter and the number of times 
#to split it when that first parameter is seen
print name.split()
print name.split("s",4)

#joins elements in parameter with variable that is calling the function
myList = ["a", "a", "g"]
s = "s"
print s.join(myList)

#replaces first parameter with second parameter, third parameter number of times
print name.replace("a", "s")
print name.replace("a", "s", 1)

#replaces placeholders in string that is calling function with parameters in order if placeholders empty
#placeholders can have index numbers that specify in what order parameters are being formatted 
date = 5
month = 3
year = 2017

todayDate = "Today's date is {2}{0}{1}"
print todayDate.format(date, month, year)

#gives length of list
print len(name)

#gives largest value based on ASCII characters for any list
namelist = ["Jasper", "Sagar", "Max", "Zebra"]
otherstring = "dddagghhhhhh"
print max(otherstring)
print max(namelist)

#gives smallest value based on ASCII characters for any list
namelist = ["Jasper", "Sagar", "Max", "Zebra"]
otherstring = "dddagghhhhhh"
print min(otherstring)
print min(namelist)

#gives index of given element in list
print namelist.index("Max")

#adds given input to end of list
namelist.append("doodoo")
print namelist

#pop removes last value in list, or one stated in input
namelist.pop()
namelist.pop(2)
print namelist

#removes first occurance of input in list 
test = [3,3,2,3,4,5,3,4]
test.remove(3)
print test

#inserts given index and object
test.insert(4,700000)
print test

#sorts smallest to largest
test.sort()
print test

#reverses order of list
test.reverse()
print test

#extends the end of a list with given value
test.extend([5,5,[5,7,[8]]])
print test