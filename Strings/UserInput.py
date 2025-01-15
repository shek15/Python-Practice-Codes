# Taking User Input
# input() method will always takes an input as a string

# After Type Casting num1 in Integer
num1 = int(input('Enter the num1 : '))
num2 = int(input('Enter the num2 : '))
print('Value of num1 is : ',num1, 'Datatype is : ', type(num1))

print('num1 after Type Casting : ',type(num1))

print(f'Addition of {num1} and {num2} is {num1 + num2}')
print(f'Substraction of {num1} and {num2} is {num1 - num2}')
print(f'Multiplication of {num1} and {num2} is {num1 * num2}')
print(f'Division of {num1} and {num2} is {num1 / num2}')