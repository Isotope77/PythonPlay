import random

# Part 3
def find(list, key):
    for item in range(len(list)):
        if list[item] == key:
            print("Found ", key," at position ",item)

# Part 4 - Pt. 1
def create_list(list_size):
    list = []
    for i in range(list_size):
        list.append(random.randrange(6))
    return list
my_list = create_list(5)
print(my_list)