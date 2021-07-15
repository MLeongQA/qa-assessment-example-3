# <QUESTION 1>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}
    
def one(items):
    item_list = set(items)
    frequency_list = []
    for list_item in item_list:
        count = 0
        for item in items:
            if list_item == item:
                count += 1
        frequency_list.append(count)
    item_dict = dict(zip(item_list, frequency_list))
    return item_dict

# <QUESTION 2>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

def two(a, b, operator):

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        return a / b

# <QUESTION 3>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
    notFound = True
    digit = num
    while notFound == True:
        if (digit ** 0.5).is_integer() == True:
            return digit
        else: 
            digit -= 1


# <QUESTION 4>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10

def four(a, b):
    if b == 0:
        return a
    else:
        return four(b, a%b)

# <QUESTION 5>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

def five(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    alphabet_list = list(alphabet)
    alphabet_list_upper = list(alphabet_upper)
    final_string = ""
    
    for character in string:
        if character in alphabet_list:
            final_string += alphabet_list[alphabet_list.index(character)-1]
        elif character in alphabet_list_upper:
            final_string += alphabet_list_upper[alphabet_list_upper.index(character)-1]
        else:
            final_string += character
            
    return final_string
