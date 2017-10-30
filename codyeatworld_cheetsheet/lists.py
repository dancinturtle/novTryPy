# len
# Similar to array.length in javascript.
# Returns count of items in list.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
len(people)
# => 5
# Returns count of characters in string.
rick = "Rick"
len(rick)
# => 4

# max
# Returns item with highest value or length.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
max(people)
# => 'Summer'

# min
# Returns item with lowest value or length.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
min(people)
# => 'Rick'

# index
# Returns lowest index found inside given object.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.index('Rick')
# => 0

# append
# Append an item into a list.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.append('Cousil Rick')
people
# => ['Rick', 'Morty', 'Summer', 'Beth', 'Jerry', 'Cousil Rick']

# pop
# Removes the last item or index from list.
people = ['Rick', 'Morty', 'Summer', 'Beth', 'Jerry', 'Cousil Rick']
people.pop()
# => 'Counsil Rick'
people.pop(0)
# => 'Rick'
people
# => ['Morty', 'Summer', 'Beth', 'Jerry']

# remove
# Returns nothing, removes item from list.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.remove('Rick')
people
# => ['Morty', 'Summer', 'Beth', 'Jerry']

# insert
# Returns nothing, add item to list at index.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.insert(1, 'and')
people
# => ['Rick', 'and', 'Morty', 'Summer', 'Beth', 'Jerry']

# sort
# Sorts list of items, can pass in compare function.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.sort()
people
# => ['Beth', 'Jerry', 'Morty', 'Rick', 'Summer']

# reverse
# Reverse items in list.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
people.reverse()
people
# => ['Jerry', 'Beth', 'Summer', 'Morty', 'Rick']

# extend
# Combine list items together into one.
people = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
earth = ["C-237"]
people.extend(earth)
people
# => ['Rick', 'Morty', 'Summer', 'Beth', 'Jerry', 'C-237']
