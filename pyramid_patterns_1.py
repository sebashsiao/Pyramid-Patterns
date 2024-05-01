# Pyramid Patterns 1
# simple way to print the pyramid

# Standard Pyramid:
print('\nStandard Pyramid:')
for i in range(5):
    print(' ' * ((5-i)-1) + '* ' * (i+1))

# Inverted Pyramid:
print('\nInverted Pyramid:')
for i in range(5):
    print(' ' * i + '* ' * (5-i))

# Left Pyramid:
print('\nLeft Pyramid:')
for i in range(5):
    print('* ' * (i+1))

# Inverted Left Pyramid:
print('\nInverted Left Pyramid:')
for i in range(5):
    print('* ' * (5-i))

# Right Pyramid:
print('\nRight Pyramid:')
for i in range(5):
    print('  ' * ((5-i)-1) + '* ' * (i+1))

# Inverted Right Pyramid:
print('\nInverted Right Pyramid:')
for i in range(5):
    print('  ' * i + '* ' * (5-i))