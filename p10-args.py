import sys

args = sys.argv
if len(args) != 2:
    print('This is not the correct format')
else:
    number = int(args[1])
    if number < 10:
        print(' It is less than 10')
    else:
        print('Something else')
