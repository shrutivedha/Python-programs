Q)  The song "99 Bottles of Beer" starts with this verse:

99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

Then the second verse is the same, except that it starts with 98 bottles and ends with 97. The song continues -- for a very long time -- until there are 0 bottles of beer.

Write a function called bottle_verse that takes a number as a parameter and displays the verse that starts with the given number of bottles.

SOLUTION

def verse():
    print("99 bottles of beer on the wall\n99 bottles of beer")

def verse2():
        print("Take one down, pass it around")
    
def bottle_verse(num):
    verse()
    verse2()


    for i in range(99,0,-1):
        i -=1
        print(f"{i} bottles of beer on the wall")

bottle_verse(99)
   
