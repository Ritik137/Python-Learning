  # we have 3 statement in transfer statement.
    # 1.break
    # 2. continue
    # 3. pass

    # 1. Break : break is use immediately even if the condition is still ture

# for i in range(1,11):
#     if i==6:
#      break

#     print(i)

# number = [10,20,30,40,50,60,70]
# for num in number:
#     if num ==50:
#         break
#     print(num)

# # Q. Stop at even number..
# numbers = [11,13,15,16,17,19,20]
# for num in numbers:
#     if num%2==0:
#         break
#     print(num)

# Q. take the number as user input, when u put 0 then the iteration stops.

# number = int(input("Enter a number: "))

# while number != 0:   
#     print("You entered:", number)    
#     number = int(input("Enter a number: "))   

# print("Loop stopped because of entered 0")

'''
# number = int(input("Enter the number"))

# while true:
#     print("Enter the number", number)
#     if number % 3 == 0 or number % 5 == 0:
#         print("Loop stop because number is divisible by 3 and 5")
#         break

#     number = int(input("Enter the number"))
'''

number = int(input("Enter the number: "))

while True:   
    print("You entered:", number)

    
    if number % 3 == 0 or number % 5 == 0:
        print("Loop stopped because number is divisible by 3 or 5")
        break

        number = int(input("Enter the number: "))
