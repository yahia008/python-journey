# adding element to a list
#append() add to the end of list-> list.append(value)
#insert() add to a specific position -> list.inset(pos, value)
#extend() add all items of one list to another list.extend(list2)

#append()
language = ['c', 'java', 'c++']

print(language)

language.append("python") # it does not create a new list
language.append(['php', 'c#'])

print(language)


#insert()

animal = ['cat', 'dog' 'fish']

animal.insert(2, 'dradon')

print(animal)

#extend()

language.extend(animal)

print(language)