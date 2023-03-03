#Lists
l = ['india', '23', '34', 'mumbai']
print(l)

#Nested lists
l = ['india', 23, [34 , 50], ('bangalore', 'delhi')]
print(l)

#indexing
l = ['india', 'mumbai', [34 , 50], ('bangalore', 'delhi')]
t =l[0]
print(t)
t = l[-3]
print(t)
t = l[-1][-2]
print(t)

#Slicing
l = ['india', 'mumbai', [34 , 50], ('bangalore', 'delhi')]
t = l[0:3]
print(t)

#membership in lists
l1 = [1,2,3,4,5,6]
print(1 in l1)
print(8 not in l1)
print(9 in l1)

#list concatenataion
l = ['mumbai', 'delhi', 'goa', 'france']
new = l + [5,3]
print(new)

#Replacing
L = ['maths', 'science', 'biology', 'chemistry', 'english']
L[1],'hindi'
print(L)

#extend
L = ['maths', 'science', 'biology', 'chemistry', 'english']
L.extend([5,6])
print(L)

#append
L = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
L.append([5, 8])
print(L)

#del command
L = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
del L[1]
print(L)

L = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
del L[0:2]
print(L)

# pop()
L = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
L.pop()
print(L)

#remove
L = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
L.remove ("Chemistry")
print(L)

#sorting list
L = [23,45,12,34,56,23]
L.sort()
print(L)

L = [23,45,12,34,56,23]
L.sort(reverse = True)
print(L)

#sort & sorted
A = ["Orange", "Strawberry", "Mango"]
B = A.sort()
print(A)
print(B)

A = ["Orange", "Strawberry", "Mango"]
C = sorted(A)
print(A)
print(C)

#Shallow copying
A = ["Orange", "Strawberry", "Mango"]
B = A
A[0] = "Apple"

A = ["Orange", "Strawberry", "Mango"]
B = A[:]
A[0] = "Apple"

L = ['one', 'two', 'three', 'four', 'five', 'six']
print(sorted(L))
print(L)