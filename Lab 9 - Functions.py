# Part 3
def find(list, key):
    for item in range(len(list)):
        if list[item] == key:
            print("Found ", key," at position ",item)
