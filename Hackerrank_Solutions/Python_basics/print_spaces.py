Q) Write a function named `print_right` that takes a string named `text` as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.

SOLUTION:
def print_right(text):
    for i in range(41):
        a = (text [:-1]) + (" " * 40) + (text[-1:])
        #result = a + b + c
    print(a)

print_right("add any string")

#for example: print_right("Right")

