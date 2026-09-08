'''
t1= (110,20,30,40,15,25,35,5,8,13,24,15)
1. Find the maximum and minimum element in the tuple.
2. count the occurence of the element in a tuple.
3. Reverse the tuple.
4. Convert this tuple to a list and add or modify an element
5. Find the third heighest element in this tuple.
'''

# answer of 1 question
t1= (110,20,30,40,15,25,35,5,8,13,24,15)
print("max is :", max(t1), "min is :", min(t1))

# answer of 2 question
print(t1.count(15))

# answer of 3 question
print(t1[::-1])

# answer of 4 question
l1 = list(t1)
l1.append(100)
l1[5] = 238
print(l1)


# answer of 5 question
x = sorted(set(t1))
print("Third highest element is:", x[-3])