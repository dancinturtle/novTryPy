# remove method can be used to remove a value from a list
# This does not return any value but removes the given object from the list.\
# Only one occurance is removed at each call.

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
print aList
aList.remove('xyz');
print "List : ", aList
aList.remove('abc');
print "List : ", aList