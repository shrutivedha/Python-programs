Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

SOLUTION


if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name,score])

    scores = sorted(set(score for _, score in students))
    second_lowest = scores[1]
    
    result = sorted(name for name, score in students if score== second_lowest)
    
    for name in result:
        print(name)
