'''
In Tuple we can store Homogeneous as well as Heterogeneous Data.
In tuple we can store Duplicates.
Tuples are ordered Collection of Data.
Tuples are Immutable: Once we declare the Tuple we cannot modify it.
'''


tup1 = (10,22.55,'Shekhar',True,10)
print(tup1)
# tup1.remove(55) --> Error
# tup1.pop()      --> Error
# del tup1[1]     --> Error
print(tup1[2])   #--> we can access

del tup1
# print(tup1) Error it deletes whole Tuple


t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2 #Concatenation
print(t3) #(1,2,3,4,5,6)