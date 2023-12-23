#logical operator is use to combile conditional expressions

#and, or, not

# in ur terminal

x = 10
y = 10
z = 30

if (x > y and y > z):
    print("x is the largest.")
else:
    print("not the largest")


x = 30
y = 10
z = 20

if (x > y or y > z):
    print("x is the largest.")
else:
    print("not the largest")

p = 10
j = 20
k = 30

if not (p > j or p > k):
    print("p is the largest.")
else:
    print("not the largest")
