#Capitalize - Capitalzie the first the first letter within a string
str_cap = 'hi this is for cap'
print(str_cap.capitalize())

#Upper - Make all the letters to Upper case
str_upper = 'hi this is for upper'
print(str_upper.upper())

#Lower - Make all the leeters to lower case
str_lower = 'HI THIS IS FOR LOWER'
print(str_lower.lower())

#Count - str.count(sub, start= 0,end=len(string)), find how many times the var occur
str_count = 'hi this is for count'
print(str_count.count("i",0,len(str_count)))

#Find - str.find(str, beg=0, end=len(string)) / The only difference betwwen find and index is that find return -1 when not found and index return ValueError
str_find = 'hi this is for index'
print(str_find.find("this"))

#Index - str.index(str, beg = 0 end = len(string)), find the index position of that var 
str_index = 'hi this is for index'
print(str_index.index("this"))

#Split - split a string base on how you want it
str_split = 'hi this is for split, have fun'
print(str_split.split(","))

#Join - Put things you want inside string
str_join1 = '-'
str_join2 = ("a","b","c")
print(str_join1.join(str_join2))

#Replace - str.replace(old, new[, max]), max is for how many times you want it to replace or it will replace all
str_replace = 'This is an example for str replace to try out, this is fun'
print(str_replace.replace("is","was",1))

#Format -  
one = 1
two = 2 
print("This is example for format {} {}".format(one,two))

#len - Output the length of that list
x = [1,2,3,4,5,6]
print(len(x))

#max - Find the max number in the list
x = [100, 50 ,70 ,40 ,60]
print(max(x))

#min - Find the min number in the list
x = [100, 50 ,70 ,40 ,60]
print(min(x))

#index - list.index(obj)
x = [100, 50 ,70 ,40 ,60]
print(x.index(50))

#append - list.append(obj)
x = [100, 50 ,70 ,40 ,60]
x.append(30)
print(x)

#pop - list.pop(obj = list[-1]) and you can assign where you want it to pop
x = [100, 50 ,70 ,40 ,60]
print(x.pop(2))
print(x)

#remove - Remove the value you want in the list
x = ["Apple",1,2,"Orange"]
x.remove("Apple")
print(x)

#Insert - list.insert(index, obj) / it wont create more space in list for you, will just put to the end
x = ["Apple",1,2,"Orange"]
x.insert(7,"Watermelon")
print(x)

#Sort - 
x = [100, 50 ,70 ,40 ,60]
x.sort()
print(x)

#reverse - 
x = [100, 50 ,70 ,40 ,60]
x.reverse()
print(x)

#extend 
x = ["Apple",1,2,"Orange"]
y = ["Up","down",10,100]
x.extend(y)
print(x)