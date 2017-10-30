# Insert an item at a given position. 
# The first argument is the index of the element before which to insert, 
# so a.insert(0, x) inserts at the front of the list, 
# and a.insert(len(a), x) is equivalent to a.append(x).

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.insert(0, 'pqr');
aList.insert(len(aList), 'pqr');

print aList
