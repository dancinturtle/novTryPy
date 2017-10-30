x = "small"
n = [10, 8, 6, 36,-3]
print x.capitalize()
print x.upper()
print x.lower()
y = ['apple', 'oranges', 'apple', 'pears', 'cucumbers']
print y.count('oranges')
z = "jonny appleseed planted {0} lots of apples {1}"
print z.find('apple')
print z.index('lots')
print z.split("planted")
s = "-"
print s.join(y)
print z.replace('apple', 'mango')
print z.format(2, "yesterday")

print len(y)
print max(n)
print min(n)
print y.index('apple')
y.append('strawberry')
print "new list: ", y
print "remove : ", y.pop(2)
y.remove('cucumbers')
print y
n.insert(2,300)
print n
y.sort()
print y
y.reverse()
print y
y.extend(n)
print "extended list : ", y