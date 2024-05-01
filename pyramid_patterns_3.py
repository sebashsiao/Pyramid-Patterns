# Pyramid Patterns 3 (Digits Pyramid)
# positional way to print the pyramid

# Standard Digits Pyramid
print('\nStandard Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:i+1]))  #:i+1 is used to slice the list
    print(f'{x:^10}')  # the expression {x:^10} is used to center the string in 10 characters
    
# Inverted Digits Pyramid
print('\nInverted Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:5-i]))
    print(f'{x:^10}')
    
# Diamond Digits Pyramid
print('\nDiamond Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:i+1]))
    print(f'{x:^10}')
for i in range(4):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:4-i]))
    print(f'{x:^10}')  # the expression {x:^10} is used to center the string in 10 characters

# Left Digits Pyramid
print('\nLeft Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:i+1]))
    print(f'{x:<10}')

# Inverted Left Digits Pyramid
print('\nInverted Left Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:5-i]))
    print(f'{x:<10}')  # the expression {x:<10} is used to left align the string in 10 characters

# Right Digits Pyramid
print('\nRight Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[:i+1]))
    print(f'{x:>10}')  # the expression {x:>10} is used to right align the string in 10 characters

# Inverted Right Digits Pyramid
print('\nInverted Right Digits Pyramid:')
for i in range(5):
    digits = [1,2,3,4,5]
    x = " ".join(map(str, digits[i:]))  # i: is used to slice the list from i to the end
    print(f'{x:>10}')  # the expression {x:>10} is used to right align the string in 10 characters
