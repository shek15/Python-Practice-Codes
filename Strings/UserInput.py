# Taking User Input
# input() method will always takes an input as a string

num1 = int(input('Enter the num1 : '))
num2 = int(input('Enter the num2 : '))
print('Value of num1 is : ',num1, 'Datatype is : ', type(num1))

# After Type Casting num1 in Integer

print('num1 after Type Casting : ',type(int(num1)))

print(f'Addition of {num1} and {num2} is {num1 + num2}')