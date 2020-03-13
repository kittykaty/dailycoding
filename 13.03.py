#Given an array of integers, return a new array such that each element at index i
#of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5],
#the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

a = int(input("Length of array: "))
list = []
for i in range(a):
    list.append(int(input("Element is: ")))
res = [i for i in range(a)]
for i in range(a):
    mult = 1
    for el in list:
        if (list.index(el) == i):
            continue
        mult *= el
    res[i] = mult
print(res)
