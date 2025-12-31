xQ7)Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description:

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string

SOLUTION:

def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line = "-".join(line)
    return(line)

