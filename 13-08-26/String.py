# 1. String is a sequence of character enclosed in a single quote, double quote, triple quote.
# 2. Strings are immutable. which means when a string is created then it cannot be changed.
# 3. It support duplicate characters
# 4. String support indexing (forward index and backword index)
#       forward index start with 0 and backward index start with -1.
# 5. Every character in the string object is represent with unique index 
# 6. Python String supports concatenation and multiplication operation.
# 7. It also support slicing operation. slicing is used to extract a part of string from the original string.

l1 = [30,40,50,60]
print(id(l1))
l1.append(60)
print(id(l1))

# Methods are in String
# 1. capitalize() - It makes the first character as uppercase.
a = "python"
b = "automation for python"

print(a.capitalize())

# 2. Upper() - It makes all the character as uppercase.
print(a.upper())
print(b.upper())

# 3. Lower() - It makes all the character as lowercase.
c="PYTHON DEVELOPER"
print(c.lower())

# 4. title() - It makes the first character of each word as uppercase.
print(b.title())

# 5. Isupper() - It checks whether all the character in the string are uppercase or not. It returns boolean value.
print(c.isupper()) 