'''
nested if
2. We use nested if when the second condition should be checked only if the first condition is true.
 syntax: if condition1:
             if condition2:
                statement
            else:
                statement
        else:
            statement

'''
# age = int(input("Enter your age:-"))
# if age >= 18:
#     if age <=100:
#         print("You are eligible for vote.")
#     else:
#         print("Invalid age.")
# else:
#     print("You are not eligible for vote.")

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username =='admin':
#     if password == 'pass123':
#         print("U are logged in successfully.")
#     else:
#         print("Invalid password.")
# else:
#     print("Invalid username.")

# 01. check a number is positive or not and then check it is even or odd.
# num = int(input("Enter a number: " ))
# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive and odd.")
# else:
#     print("The number is not positive.")

# ----------------------------------------------------------------------------------------------------
# 02. a student is eligible for exam if attendance is least 75% and marks are atleast 40%.
# attendance = float(input("Enter your attendance percentage: "))
# marks = float(input("Enter your marks percentage: "))

# if attendance >= 75:
#     if marks >= 40:
#         print("The student is eligible for the exam.")
#     else:
#         print("The student is not eligible for the exam due to insufficient marks.")
# else:
#     print("The student is not eligible for the exam due to insufficient attendance.")

# ----------------------------------------------------------------------------------------------------
# 3. Take a number if positive then check whether it is even or odd. if negative then check whether it is divisible by 3. if zero then print "zero"
# num = int(input("Enter a number: "))
# if num > 0: 
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("the number is positive and odd.")
# else:
#     if num < 0:
#         if num % 3 ==0:
#             print("The number is negative and divisible by 3.")
#         else:
#             print("The number is negative and not divisible by 3.")
#     else:
#         print("The number is zero.")

# ----------------------------------------------------------------------------------------------------
# 04. take a number if it is even , check whether it is divisible by 4. if it is odd check whether it is divisible by 3.
num = int(input("Enter a number: "))
if num % 2 ==0:
    if num % 4 ==0:
        print("The number is even and divisible by 4.")
    else:
        print("The number is even but not divisible by 4.")
else:
    if num % 3 ==0:
        print("The number is odd and divisible by 3.")
    else:
        print("The number is odd but not divisible by 3.")

# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------

