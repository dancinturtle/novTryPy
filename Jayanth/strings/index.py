# It determines if string str occurs in string, or in a 
# substring of string if starting index beg and ending index end are given.

simpleSentence = "Hi, this is Jayanth Kanive. People call me Jayanth"

findStr = "Jayanth"

print simpleSentence.find(findStr)
print simpleSentence.find(findStr,0,21)
print simpleSentence.find(findStr,13)