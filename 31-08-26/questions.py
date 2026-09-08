'''
1. Remove all the spaces from the beginning and end of the text
text = ' Python is very easy '
2. s1={10,20,30,40,50}
    s2={30,40,50,80,90,15}
    find the difference between two sets.

3. Check whether one set is subset of other.
4. remove all element from a set
5. student={'name':'sankar','age':29,'city':'Puri'}
    add 'course':'Pyton' using a dist method
6. remove city using dict method
7. get all keys using a dict method.
8.check whether 'salary' exists using a dict method
9. remove the course key value.
10. language=['python','java','c++','javascript']
    insert 'ruby' at index 2.
11. delete the last element.
''' 

# Answer of the QUESTIONS.
# 1. Remove all the spaces from the beginning and end of the text
# text = ' Python is very easy '
text = ' Python is very easy '
a = text.strip()
print(a)

# 2. s1={10,20,30,40,50}
    # s2={30,40,50,80,90,15}
    # find the difference between two sets.
s1={10,20,30,40,50}
s2={30,40,50,80,90,15}
b = s1.difference(s2)
print(b)

# 3.  Check whether one set is subset of other.
c = s1.issubset(s2)
print(c)

# 4.  remove all element from a set
d = s1.clear()
print(s1)

# 5. student={'name':'sankar','age':29,'city':'Puri'}
#     add 'course':'Pyton' using a dist method

student={'name':'sankar','age':29,'city':'Puri'}
student.update({'course':'Python'})
print(student)

# 6. remove city using dict method

f = student.pop('city')
print(f)
print(student)

# 7. get all keys using a dict method.

g = student.keys()
print(g)

# 8.check whether 'salary' exists using a dict method

h= student.get('salary')
print(h)

# 9. remove the course key value.

i = student.pop('course')
print(i)
print(student)

# 10. language=['python','java','c++','javascript']
#     insert 'ruby' at index 2.

language=['python','java','c++','javascript']
language.insert(2,'Ruby')
print(language)

# 11. delete the last element.

language.pop(-1)
print(language)