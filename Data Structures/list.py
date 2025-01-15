'''
1. In List we can store Homogeneous as well Heterogeneous Data.
2. In Lis we can store Duplicate Values.
3. List is an Ordered Collection of Data: Order of insertion will
   remain as it is in the Output.
4. Lists are Mutable: Once we declare the list we can modify it.
'''
li1 = [10,20,44,45,20,True,'Shekhar']
print(li1, type(li1))

# After Appending Value at last

li1.append(300)
print('After Adding value : ', li1)

# After Inserting Value ---> insert(idx, ele)

li1.insert(1,15)
print('After Adding value at given index : ', li1)


# After Removing Value ---> remove(ele) remove first occurence

li1.remove(20)
print('After Removing value at given index : ', li1)

# in and not in Operator:

print(2000 in li1) #False
print('Shekhar' in li1) #True


# pop(): Remove and Return last Element

li1.pop()
print("After Poping out Element: ",li1)

# del keyword : del ---> delete only not return

del li1[1]
print("After Deleting value at Specified idx: ", li1)

del li1
# print(li1) Error we deleted whole list