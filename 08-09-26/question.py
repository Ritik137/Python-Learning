'''
1. Take a string from the user. if the string is empty, print 'Empty string'.otherwise
, check whether its length is greater than 5 and print 'long' or 'short'.
2. Take a string and check whether it is a palindrome or not.
3. fruits=['apple','banana','mango','orange']
Ask the user for a fruit. if it exists in the list check whether it is 'mango' and print
'special fruit', otherwise print 'Available'.
4. employee={
'name':'Rahul',
'department': 'QA',
'experience':4}
check whether 'department' exists.
if exists, check whether the department is 'QA'.
if QA, check whether experience is greater than or equal to 3.
print 'Eligible for Automation project' or 'Not eligible'.
5. numbers=[10,20,30,40]
take a number from the user.
first check whether it exists in the list.
if exists, check whether it is greater than 25.
if greater than 25, check whether it is divisible by 10
print 'valid number','greater but not divisible by 10','25 or below',or 'not found'.

'''

# 1. Take a string from the user. if the string is empty, print 'Empty string'.otherwise
# , check whether its length is greater than 5 and print 'long' or 'short'.

# String = input("Enter a string: ")
# if not String:
#     print("Empty String.")
# else:
#     if len(String)> 5:
#         print("Long")
#     else:
#         print("Short")

# 2. Take a string and check whether it is a palindrome or not.
# String = input("Enter a string: ")

# if String == String[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# 3. fruits=['apple','banana','mango','orange']
# Ask the user for a fruit. if it exists in the list check whether it is 'mango' and print
# 'special fruit', otherwise print 'Available'.

# fruits = ['apple','banana','mango','orange']

# fruit = input("Enter name of fruit :")

# if fruit in fruits:

#     if fruit == "mango":
#         print("Special fruit")
# else:
#     print("Available.")


# 4. employee={
# 'name':'Rahul',
# 'department': 'QA',
# 'experience':4}
# check whether 'department' exists.
# if exists, check whether the department is 'QA'.
# if QA, check whether experience is greater than or equal to 3.
# print 'Eligible for Automation project' or 'Not eligible'.

# employee={
# 'name':'Rahul',
# 'department': 'QA',
# 'experience':4}

# if 'department' in employee:
#         if employee['department'] == 'QA':
#                 if employee['experience']>=3:
#                         print("Eligible for Automation project")
#                 else:
#                         print("Not Eligible")



# 5. numbers=[10,20,30,40]
# take a number from the user.
# first check whether it exists in the list.
# if exists, check whether it is greater than 25.
# if greater than 25, check whether it is divisible by 10
# print 'valid number','greater but not divisible by 10','25 or below',or 'not found'.

# numbers =[10,20,30,40]
# number = int(input("Enter a number :"))
# if number in numbers:
#     if number > 25:
#         if number % 10 == 0:
#             print("Valid number..")
#         else:
#             print("greater but not divisible by 10")
#     else:
#         print("25 or below")
# else:
#     print("not found..")