student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
for n in student_heights:
    count += 1

total = 0
for c in range(1, count + 1):
    total += student_heights[c - 1]

average = round(total / count)
print(average)