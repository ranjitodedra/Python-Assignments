# NAME : Odedra Ranjit Jakharbhai
# ID : 20CE062


#-------(A).Write a Python program to add member(s) in a set and clear a set
SET = {'H', 'e', 'l', 'l', 'o'}
SET.add('!')
print("Letters are:", SET)
print("Set before clear:", SET)
print("Set after clear:", SET.clear())


#------------(B).Write a Python program to remove an item from a set if it is present in the set.
set = {'H', 'e', 'l', 'l', 'o'}
set.remove('o')
print("Letters are:", set)

#------------(C).Write a Python program to create an intersection, Union, difference of sets.
set2={2,4,5}
set3={4,6,7,9}
print("Union of two sets:", set2.union(set3))
print("Intersection of two sets:", set2.intersection(set3))
print("Difference of two sets:", set2.difference(set3))

#-----------(D).Write a Python program to find maximum and the minimum value in a set.
set = {1, 2, 3, 4, 5}
print(min(set))
print(max(set))


#-----------(E).Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# Most comman element in list
list1=[1,3,5,1,2,3,2,6,2]
comman=max(list1, key=list1.count)
print("Most comman element in list is", comman, "and its count is :", list1.count(comman))

# Most comman element in tuple
tuple1=(10, 20, 30, 40, 20)
comman=max(tuple1, key=tuple1.count)
print("Most comman element in tuple is", comman, "and its count is :", tuple1.count(comman))

# Most comman element in dictionayr
dic1=[1, 2, 3, 4, 2, 1, 6, 1, 1]
comman=max(dic1, key=dic1.count)
print("Most comman element in dictionary is", comman, "and its count is :", dic1.count(comman))
