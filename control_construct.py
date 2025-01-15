'''
1. Conditional : if-else, if-elif
2. Looping : for, while
3. Jumping : break, continue, pass
'''

# def checkAge(age):
#     if(age > 18):
#         print('Age is greater than 18')
#     else:
#         print('Age is not greater than 18')

# checkAge(25)

# WAP to display 'Child' if age < 18, if age > 18 AND age < 65 'Adult'
# if age > 65 'Senior Citizen'

# def age_category(age):
#     if(age < 18):
#         print('Child')
#     elif(age < 65):
#         print('Adult')
#     else:
#         print('Senior Citizen')

# age_category(70)

# --------Looping--------

'''
for control_variable in iterable_object 
'''

# for i in 'Shekhar':
#     print(i, end='-')

# print('\n--------------')

# for j in [1,2,3,4,5]:
#     print(j, end='-')

# print('\n--------------')

# for num in range(1,10):
#     print(num,end='-')

# range(init_val,end_val,steps)
# init_val ---> starting value
# end_val ----> ending value which is not included
# steps ------> how many steps want to jump to get next value

# for num in range(5):
#     print(5) # print 5 --> 5 times


'''
While Loop
'''

# i = 0
# while(i<10):
#     print(i+100)
#     i = i+1

# WAP print 1-10 but skip 6
# WAP print 1-10 but stop when getting 5

# for i in range(1,11):
#     if (i == 6):
#        continue
#     else: 
#         print(i)

# print('--------------------')

# for i in range(1,11):
#     if (i == 5):
#        break
#     else: 
#         print(i)