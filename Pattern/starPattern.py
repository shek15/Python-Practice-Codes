# ----------Square Pattern---------
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# row = 4
# col = 5
# for i in range(row):
#     for j in range(col):
#         print('*', end=" ")
#     print()


# ---------increasing Triangle-------------
'''
*
* *
* * *
* * * *
* * * * *
'''


# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()


# # -----------Decreasing Triangle-------------------
'''
* * * * *
* * * *
* * *
* *
*
'''

# row = 5
# for i in range(row):
#     for j in range(row-i):
#         print("*",end=" ")
#     print()


# -----------Pascle Triangle-------------------
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

# row = 5
# for i in range(row):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(row):
#     for j in range(row-i):
#         print("*",end=" ")
#     print()


# -----------Pascle Triangle-------------------
'''
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
'''

# row = 5
# for i in range(row):
#     for j in range(row*2):
#         if(j <= i):
#             print("*",end=" ")
#         elif(j<row*2 - (i+1)):
#             print(" ", end=" ")
#         else: print("*",end=" ")
#     print()

# row = 5
# for i in range(row):
#     for j in range(row*2):
#         if(j <= row-(i+2)):
#             print("*",end=" ")
#         elif(j<=row+i):
#             print(" ", end=" ")
#         else: print("*",end=" ")
#     print()


# -----------Daimond Triangle-------------------
'''   
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *        
 * * * * * * * * *
* * * * * * * * * * 
 * * * * * * * * *
  * * * * * * * *
   * * * * * * *
    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''


row = 5
for i in range(row):
    for j in range(row*2):
        if(j <= row-(i+1)):
            print(" ",end=" ")
        elif(j<=row+i):
            print("*", end=" ")
    print()

row = row
for i in range(row):
    for j in range(row*2):
        if(j <= i):
            print(" ", end=" ")
        elif(j <= (row*2)-(i+1)):
            print("*",end=" ")
    print()


# Interview Questions

for y in range(1,11):
    Z = 200

def disp(a):
    print(a) #50
    y = 100
    print(y) #100

disp(50)