course = {'name':'python', 'instructor':"yahya"}


for i in course:
    print(course[i])

for y in course.values():
    print(y)

for x, z in course.items():
    
    print(x, y)

list1 = [1, 2, 3]

list2 = [4, 5, 6]

for i in list1:
    for j in list2:
        print(i, j)
    print()