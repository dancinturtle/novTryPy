characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
for person in characters:
    #.upper prints all the letters in the string into uppercase
    print person.upper()
    #.capitalize capitalizes just the first letter of each string
    print person.capitalize()
    #.lower prints all the letters in the string into lowercase
    print person.lower()

mycount= "coding dojo"
sub= "d"
sub1="b"

#.count returns the number of repetition for "sub" within the string
print mycount.count(sub)

#.find returns the index of the first iteration of "sub" within the string
print mycount.find(sub)

#.index same as .find but if index is outside of string length returns value error
print mycount.index(sub)

#.split returns a list of values where the string is split at the given character. without a parameter the splits are assumed at each space
print mycount.split()

#.replace replaces the first parameter with the second parameter
print mycount.replace("dojo","us")

# format replace {} with the value of varible passed into format
print "This is the format example {}".format(mycount)
#expected output is "This is the format example coding dojo"

#.join returns a string of concated items from the list
print person.join(characters)


#List Methods Below

#.len returns the number of items in the list
print len(characters)

#.max returns the largest or longest item in the list
print max(characters)

#.min returns the smallest or shortest(alphabetical order if multiple) item in the list
print min(characters)

#.index returns the index of the parameter
print characters.index("Morty")

#.append appends the parameter into the list at the end
characters.append("Jinal")
print characters

#.pop removes the item at the specified index, if no parameter is given will remove last index.
characters.pop(3)
print characters

#.remove removes specified item(s) from the list
characters.remove("Morty")
print characters

#.insert inserts second parameter into the index specified via the first parameter
characters.insert(3, "Dalina")
print characters

#.sort returns the list with items sorted numerically or alphabetically
characters.sort()
print characters

#.reverse returns the list with items within the index in reverse order
characters.reverse()
print characters

#.extend returns the list with the parameter appended at the end
characters1 = ["Patel", "Wayne","Dao"]
characters.extend(characters1)
print characters