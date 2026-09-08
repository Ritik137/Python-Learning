# 1. Reverse a string s = 'python is very easy'  o/p ='easy very is python'
# 2. Find the 2nd largest number in a list l = [10,20,30,40,15,25,35,5,8,13,24]
# 3.l=[10,20,30,40,['py','java','c','[2,3,4,'hari'],60],80,90] find the index number of hari
# 4. find out the smallest value in a list l=[10,20,30,40,15,25,35,5,8,13,24]
# 5. sort the list in descending order l =[10,20,30,40,15,25,35,5,8,13,24]

# answer of 1 question
s = 'python is very easy'
word = s.split()
word.reverse()
result = ' '.join(word)
print(result)

# answer of 2 question
l = [10,20,30,40,15,25,35,5,8,13,24]
l.sort()
print(l[-2])

# answer of 3 question
l = [10,20,30,40,['py','java','c',[2,3,4,'hari'],60],80,90]
print(l[4][3][3])

# answer of 4 question
l = [10,20,30,40,15,25,35,5,8,13,24]
print(min(l))

# answer of 5 question
l = [10,20,30,40,15,25,35,5,8,13,24]
l.sort(reverse=True)
print(l)