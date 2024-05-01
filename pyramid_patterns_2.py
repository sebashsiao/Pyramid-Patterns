# Pyramid Patterns 2
# positional way to print the pyramid

# Standard Pyramid
print('Standard Pyramid:')
for i in range(5):
    x = "* " * (i+1)
    print(f'{x:^10}')
    
# Inverted Pyramid
print('\nInverted Pyramid:')
for i in range(5):
    x = "* " * (5-i)
    print(f'{x:^10}')
    
# Diamond Pyramid
print('\nDiamond Pyramid:')
for i in range(1,6):
    x = "* " * i
    print(f'{x:^10}')
for i in range(1,6):
    x = "* " * (5-i)
    print(f'{x:^10}')  # the expression {x:^10} is used to center the string in 10 characters

# Left Pyramid
print('\nLeft Pyramid:')
for i in range(1, 6):
    x = "* " * i
    print(f'{x:<10}')  # the expression {x:<10} is used to left align the string in 10 characters

# Left Inverted Pyramid
print('\nLeft Inverted Pyramid:')
for i in range(5):
    x = "* " * (5-i)
    print(f'{x:<10}')  # the expression {x:<10} is used to left align the string in 10 characters

# Right Pyramid
print('\nRight Pyramid:')
for i in range(1,6):
    x = "* " * i
    print(f'{x:>10}')  # the expression {x:>10} is used to right align the string in 10 characters

# Right Inverted Pyramid
print('\nRight Inverted Pyramid:')
for i in range(5):
    x = "* " * (5-i)
    print(f'{x:>10}')  # the expression {x:>10} is used to right align the string in 10 characters
