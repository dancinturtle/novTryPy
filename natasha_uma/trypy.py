#to get the total length of a list i can use the len method and passing my variable such as:
my_num = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]

print len(my_num)

#to get the max value in a list, the max method can be used by passing in the variable 
my_list = [9,4,3,6,10,54,89,2,4,1034,1095]

print max(my_list) 

#to get the min value in a list, the max method can be used by passing in the variable 
my_list = [9,4,3,6,10,54,89,2,4,1034,1095]

print min(my_list) 

#to get the lowest index of an object in a list, the index method can be used
#to use the index method, the method is attached to the variable and then the obj is passed in the parameter 
natasha = [9, "hello", 10, 56, 18, "hello", "no", "no", "no", 14, "yes"]

print natasha.index("no")

#the append method will add any given value that is passed at the end of a list such as -
listy = ["great",12,3,4,5,6,65,67,34,2,4,6,"rgre"]
listy.append(30)

print listy

#pop method is used to remove the last object from a list unless an index is passed in a parameter
#the removed object will be returned 
listys = ["great",12,"rgre"]
listys.pop(1)

print listys

#remove method gets rid of the first matching obj that is passed in the parameter. index is not a factor
listys = ["great",12,"rgre"]
listys.remove("great")

print listys

#insert method inserts the obj you pass into the index of a list you pass as well 
#this extends the list since the obj at the index isn't being replaced; rather just inserted at that index 
#pushing the remaining objs over one 
listc = [1,2,3,4,5,6,7]
listc.insert(2, "i am inserting myself hehehe")

print listc

#sort method sorts the objs in a given list from lowest in value to highest 
#if the list has a combo of integers and strings, the integers will be sorted at the begeinning 
#the the strs are sorted based on first letter of str and it's place in the alphabet
listd = [45,87,43,2,57,43,"great","abc","fbg","lolololol","no"]
listd.sort()

print listd

#reverse method reverses the order of the objs in any given list 
liste = [1,2,3,4]
liste.reverse() 

print liste  

#extend method is essentially a concatenator for lists. it will append the values of the variable or obj passed 
# in the parameter to the given variable 
lista = [1,2,3]
listb = [4,5,6]
lista.extend(listb)

print lista 