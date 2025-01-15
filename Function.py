# Without input and without return statement
def add():
    a = 10
    b = 20
    print('Addition : ',a+b)

add()

# ---------------------------------------------

# With input & without return
def sub(a,b):
    print('Subtraction : ',a-b)

# ---------------------------------------------

# Without input & with return
def mul():
    return 10*20

# ---------------------------------------------

# with input & with return statement
def div(a,b):
    return a/b

# ---------------------------------------------

add()
sub(100,50)
print(mul())
print(div(200,10))