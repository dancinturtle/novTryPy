characters = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
for person in characters:
    print person.upper()
    print person.capitalize()
    print person.lower()

mycount= "coding dojo"
sub= "o"
sub1="b"
print mycount.count(sub)
print mycount.find(sub)
print mycount.index(sub)
print mycount.split()
print mycount.replace("dojo","us")

# format replace {} with the value of varible passed into format
print "This is the format example {}".format(mycount)
#expected output is "This is the format example coding dojo"

print person.join(characters)

print len(characters)
print max(characters)
print min(characters)
print characters.index("Morty")
characters.append("Jinal")
print characters

characters.pop(3)
print characters

characters.remove("Morty")
print characters

characters.insert(3, "Dalina")
print characters

characters.sort()
print characters

characters.reverse()
print characters

characters1 = ["Patel", "Wayne","Dao"]
characters.extend(characters1)
print characters