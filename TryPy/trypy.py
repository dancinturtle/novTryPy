#STRINGS

# to capitalize each first letter in the word use .capitalize() method, with the string before .capitalize
characters = "rick"
print characters.capitalize()
#returns Rick

#returns a copy of the whole string in uppercase
print characters.upper()
#returns RICK

#.lower() returns a copy of the string converted completely to lowercase
print characters.lower()
#returns rick

#count returns the number of occurances of the substr in original string. Uses (str[start:end]) as paramaters.
#defaults start and end to 0
string ="today is my birthday"
strg= "day"
print string.count("day")
#returns 2

#.find() returns lowest index at which substring is found. (str[start:end]) start and end default to entire string
#-1 on failure
print string.find(strg)
#returns 2, as "day" begins  on 2nd index of the string

#.index() is similar to .find(), but returns ValueError when not found
print string.index("day")
#returns 2

""".split() reutrns a list of words of the string. (str[, sep[, maxsplit]]) are parameters. By default 
they separate with whitespace, but 'sep' can replace a string as the separateor. 
maxsplit defaults to 0, but that number specifies how many splits will occur at most"""
string ="today is my birthday"
print string.split("y")

#.join() concentrates a list or words to string at intervening occurances of sep (default whitespace)
string2 ="today is my birthday"
print string2.join("now")
# returns: ntoday is my birthdayotoday is my birthdayw (wraps each character of "now around" occurances of string2)

#replaces occurances of first argument within string with second argument
print string.replace("day", "month")
#returns tomonth is my birthmonth

#.format() formats string with replacement holders
string3 = "The sum of 1 + 2 = {}"
print string3.format(1+2)
#returns The sum of 1 + 2 = 3


#NUMBERS


