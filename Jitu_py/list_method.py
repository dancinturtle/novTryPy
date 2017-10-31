#len

my_list = [1,2,3,4,5,6,7,8,9,22]
vowoels = ['a','e','o','i','u']
print len(my_list)
my_list.append(22)
my_list1 = [1,2,3,4,5,6,7,8,9,22]
my_list1.pop(2)
my_list3 = ['jitu','dojo','jquery','php']
my_list3.remove('php')
my_list4 =[1,2,6,5]
my_list4.insert(2,'3')
my_list5 = [2,5,1,9]
my_list5.sort()
os = [12,113,55,65]
os.reverse()
my_list.extend(os)

#max
print max(my_list)

#min

print min(my_list)

#index

print vowoels.index('e')

#append
print "updated list :", my_list

#pop

print "updated list :", my_list1
#remove
#The remove() method searches for the given element in the list and removes the first matching element.
print my_list3

#insert
#insert() method inserts the element to the list at the given index.
print my_list4

#sort
#sort() method sorts the elements of a given list.
print my_list5


#reverse
#reverse() method reverses the elements of a given list.
print os

#extend
#extend() extends the list by adding all items of a list (passed as an argument) to the end
print my_list