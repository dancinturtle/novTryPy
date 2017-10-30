#STRING METHODS:


#capitalize will take a string and capitalize the first word
cat = "the cat in the hat"
print cat.capitalize()

#upper  will Capitalize all letters in a string.
var = 'The long wall is a hard run'
print var.upper()

#lower will return all letters in a string as lower case.
words = 'Words, Words, Words'
print words.lower()

#count will tally all the instances of a substring within a string
string= 'there all kinds of words. words, words words.'
string.count('words')

#find will find a substring in a string and share the first instance and return the position before's value.
find= 'the little kid lost his little bike'
find.find('little')

#The "index" string method returns the index location within the string where the value/substring starts
#the following example will tell us at what index the letter "q" is in the string called "alphabet"
alphabet = "abcdefghijklmnopqrstuvwxyz"
print alphabet.index('q')
#The "split" string method returns a list of values split by the indicated value.
#The default value splits the string at any spaces between characters.
#The following example will show the default split of the string, and then using a specified value
wisdom = "A fool and his money are soon parted."
print wisdom.split()
print wisdom.split('o')
#The "join" string method returns a string in which string elements from a secondary string
#are concatenated with the strings in sequence.
#The following example will show the strings in a list being "joined" with an existing string.
#then it will show a single string being "joined" with the existing string.
separator = "--"
more_words = ["This", "is", "good", "advice."]
other = "abcdefg"
print separator.join(more_words)
print separator.join(other)
#The "replace" string method returns a copy of the string where the occurrences of an "old"
#values are replaced with a "new" value, and an optional parameter can limit the # of replacements
#The following example will show replacement of elements in a string with new elements, and then
#return another string. One example will be unlimited, the other will pass a thrid parameter to limit
#the replacements.
silly = "this this this this this"
print silly.replace("this", "you")
print silly.replace("this", "you", 2)
#The "format" string method helps when printing strings, and eliminates the confusion of concatenation.
#Placeholders in a string are set with curly brackets {} indicating the position that the elements
#in the format () parentheses will print.
#The following example will show the elements in the format parentheses printed in the string
first_name = "Humphrey"
last_name = "Bogart"
print ("{} {} was a great actor.").format("Paul", "Newman")
print ("{} {} was a great actor.").format(first_name, last_name)

#LIST METHODS


#To find the length of a string, list, or tuple, use the len() function.
#The following code will print the len of the following list of GoT characters
characters = ["Danaerys", "Jon", "Brienne", "Jamie", "Cersai", "Robert"]
print len(characters)

#To find the maximum value within a list, use the max() function.
#The following code prints the maximum value within a given array of home values
values = [322222,450000,500000,1000000,2000000,150000]
print max(values)

#To find the minimum value within a list, use the min() function.
#The following code prints the minimum value within a given array of home values
values = [322222,450000,500000,1000000,2000000,150000]
print min(values)

#The index function finds the index position of the first occurence of a given value.
#For exmample, the code below finds the index position of the the camper "Nathan" within a given list of campers
campers = ["Angela", "Dave", "Ralph", "Paul", "Nathan", "Hugh", "Arnold", "Cynthia"]
print campers.index("Nathan")

#To add a value on to the end of a list, use the append method.
#The following code adds the additional camper of "Beth" to a list to the end of a list of campers, and then prints the updated list
campers = ["Angela", "Dave", "Ralph", "Paul", "Nathan", "Hugh", "Arnold", "Cynthia"]
campers.append("Beth")
print campers

#Use pop to remove a value of an array located at a particular index
#If no index is specified, the last item within the array will be removed by default
#In the code below, the the camper "Dave" is removed from the list, using the pop method.
campers = ["Angela", "Dave", "Ralph", "Paul", "Nathan", "Hugh", "Arnold", "Cynthia"]
#first the index of "Dave" is located using the index method. Then the index is "popped" using the pop method.
campers.pop(campers.index("Dave"))
print campers

#List.Remove()
#characters.remove(element) will remove anything inside of this character list
#if there is a item on the list that matches the element for exmaple this list
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print characters
#I want to remove Summer, So i remove it using the following command
characters.remove("Summer")
print characters

#How to insert into list
#in order to insert an item into a list, you need to give both the index and the elemtn you have to add.
#The Index will indicate where in the lis tit will add the element you are giving the method.
#for Example with this given list
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print characters
#I want to add My name, Jesus, on the third slot.
characters.insert(2, "Jesus")
print characters

#How to sort List
#A list is sorted with the sort or a sorted method.
#Sort has to be called with a . next to the list and can take up to 2 parameters. The two parameter are key and reverse.
#A list can be sorted in reverse and on key values. Keys are more for objects, So I will skip that for now.
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print characters
characters.sort()
print characters

#with no paramters this will sort in in alphabetical order. If I were to make reverse true. The reverse will happen
characters.sort(reverse=True)
print characters
#Sorted is the same thing but instead you are calling the list inside the method as a parameter.
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print characters
print sorted(characters, reverse=True)

#Extend adds another list into the same list by extending the list and making it apart of the original list.
characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print characters
characters.extend(characters)
print characters