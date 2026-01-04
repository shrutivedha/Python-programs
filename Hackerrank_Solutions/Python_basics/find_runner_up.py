Q) Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up. 

SOLUTION:

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

first = float('-inf')
runner_up = float('-inf')

for num in arr:
    if num > first:
        runner_up = first
        first = num
    elif num < first and num > runner_up:
        runner_up = num

print(runner_up)
