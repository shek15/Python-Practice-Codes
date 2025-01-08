# Strings are Immutable:
# 1. Once we declare the string we cannot modify it, 
# if we try to modify the string it will create new string

# 2. If new string does not have any reference variable, 
# PVM will collect the string in garbage

# 3. Python Internally uses String Interning.

# 4. String Interning is the Process  of Checking string Intern Pool
#  before Creating any new object.

# 5. Whenever we want to create new object, Python first will check string
# intern pool, whether that object already exist or not.

# when Object already exist in the string inter Records then address of
# existing object will be reused.

# s1 = 'Kodnest'
# s1 = s1.upper()
# print(f'The modified s1 is : ', s1)

# s1 = 'K'
# print(f'The Memory Address of s1 : ', id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print(s1[2], id(s1[2]))
print(s2[-2], id(s1[-2]))