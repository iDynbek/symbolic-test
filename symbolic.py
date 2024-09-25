# problem:
# write a symbolic interpretator for python using classes and tuples, this interpretator should be able to perform algebraic operations between TWO expressions
# let's say we have an expression of the type: 5 x^5 + 9 x y
# this can be stored as following list:
# [[(5,'x',5)],[(9,'x',1), (1,'y',1)]]
# the logic is following:
# expression is a list where each object is a term
# term is a list where each object is a variable
# variable is a tuple where the first object is a numerator, second one is a variable symbol, and third one is the power

# now we need to perform algebraic operations of type expression1 OPERATION expression2
# where expressions can be any type of mathematical expression

# this type of program also needs to follow the convention of algebraic operation:
# 1. parentheses
# 2. exponential
# 3. multiplication and division
# 4. addition and substraction

# SOLUTION
# first step is to declare our objects:

expression1 = []
expression2 = []

# now we create a function that reads our input and stores it in
# it is possible to write a simpler code using re library, but for fun let's try to write it using pure python
def read_expression(x):
# first we check whether the input is a string:
    if isinstance(x, str)==False:
        print('Input is not a string!')
        return

# following piece of code finds the first leftmost operand in the expression:
    index=0
    while index != -1:
        index_plus = x.find('+')
        index_minus = x.find('-')
        index_multiply = x.find('*')
        index_divide = x.find('/')
        


# expression reads the input string and stores it in a container described above



# now that we stored our expression into our class, we can start performing mathematical operations:

#def add(x):

#def multiply(x):

#def divide(x):


# now let's write a function that solves our expression:
#def solve(x):