# if string is holding integer then it can be converted into int 
# a = '30'
# print(a,type(a))
# b = int(a)
# print(b,type(b))

# ---------------------------------------------

# x = 'Kod'
# print(x,type(x))

# str to integer conversion is not allowed
# y = int(x)
# print(y,type(y))

# ---------------------------------------------

# p = float(input('Enter Float type data : ')) #12.22
# print(p,type(p))

# ---------------------------------------------

# 1. While converting int to bool 
# for all non-zero value we will get true

# 2. While converting int to bool for 0 and empty strings
# we will get false 

q = 'Shekhar'
print(q,type(q))
q = bool(q)
print(q,type(q))

# ---------------------------------------------

#  '12.56' ----> Error & 12.56 -----> 12

# print(int('12.56')) 
print(int(12.56))