
x = [2,54,-2,7,12,98]

#max value in array
print "Max value is : ", max(x)

#min value in array
print "Min value is : ", min(x)

#length of given array
print len(x)

#index of given array
print "Index for -2 : ",x.index(-2) 

#append the number -77 to an array
x.append(-77)
print "Updated List : ", x

#append the string to an array
x.append('hello')
print 'Added the string : ', x

#pop the value in the array
x.pop(3)
print "New array wihtout value of index 3 : ", x

#removing all negative numbers
x.remove(-77 and -2)
print "Removed negative numbers : ", x

#insert number to index 4
x.insert( 4, 2017)
print "New list with inserted number to index [4] : ", x

#sort an array
x.sort()
print "Sorted Array : ", x

#revers an Array
x.reverse()
print "Reversed array : ", x

#extend an array
y = ['coding', 'dojo', 2017]
x.extend(y)
print "Extended List : ", x





