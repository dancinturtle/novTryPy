# capitalize
# Return a copy of the string with only its first character capitalized.
"my lowercase string".capitalize()
# => "My lowercase string"

# upper
# Return a copy of the string with lower case letters converted to upper case.
"codingdojo".capitalize()
# => "CODINGDOJO"

# lower
# Return a copy of the string but with upper case letters converted to lower case.
"CODINGDOJO".lower()
# => "codingdojo"

# count
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
# Optionally pass in a start and end.
fruits = "Bananas, Mangos, Pineapples."
fruits.count('a')
# => 5
fruits.count('a', 7)
# => 2

# find
# Returns the index at the first occurrence.
veggies = "Brocoli, Carrots, Peas."
veggies.find('Carrots')
# => 9

# index
# The difference is that find returns -1 when what you're looking for isn't found. index throws an exception.
lottery = [1, 2, 3, 4, 5]
lottery.index(1)
# => 0

# split
# Split a string into an array using a delimiter.
# Returns a copy.
fruits = "Bananas, Mangos, Pineapples."
fruits.split(' ')
# => ['Bananas', 'Mangos', 'Pineapples.']

# join
# Join an array together using a spacer.
fruits = ['Bananas', 'Mangos', 'Pineapples.']
'<--->'.join(fruits)
# => 'Bananas<--->Mangos<--->Pineapples.'

# replace
# Find and replace.
# Pass in a max to stop affter count.
sentence = "This is a sentence that is long and likes to run on."
sentence.replace('is', 'hello')
# => 'Thhello hello a sentence that hello long and likes to run on.'
sentence.replace('is', 'hello', 1)
# => 'Thhello is a sentence that is long and likes to run on.'

# format
# String interpolation and padding/alignment.
'{} {}'.format('hello', 'world')
# => 'hello world'
# Padding left
'{:>10} {}'.format('hello', 'world')
# '     hello world'
'{} {:10}'.format('hello', 'world')
# Padding right
# => 'hello world     '
# You are able to choose the padding character:
'{} {:_<10}'.format('hello', 'world')
# => 'hello world_____'
'{:_>10} {:_<10}'.format('hello', 'world')
# => '_____hello world_____'
