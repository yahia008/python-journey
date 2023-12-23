# list comprehension

names = ['john', "jimmy", "james", "micheal", "emmy" ]

j_names = []

for name in names:
    if ('j' in name):
        j_names.append(name)

print(j_names)


# we can achive same functionality with list comprehension 

j_names  = [name for name in names if 'j' in name]

print("new", j_names)
