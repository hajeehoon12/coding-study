import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    input_data = sys.stdin.readline().split()

    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key =lambda student: student[1])

for student in array:
    print(student, end = ' ')
    
for student in array:
    print(student[0], end = ' ')