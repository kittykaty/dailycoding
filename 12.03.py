#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#[10, 15, 3, 7]
#17

def yes(list, k):
    for i in list:
        for j in list:
            if (i == j):
                continue
            if (i + j == k):
                return True
    return False


list = []

size = int(input("Number of elements: "))
for i in range(0, size):
    i = int(input("Element of list: "))
    list.append(i)
print(list)

k = int(input("Input k: "))
print(yes(list, k))
