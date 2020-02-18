# ques 7:program to display letters that are not common in both strings.

list1 = [2, 5, 8, 10]
list2 = [4, 3, 2, 6, 8, 9, 1]

for element in list2:
    if element in list1:
        list2.remove(element)

print("After removing common elements: ", (list1+list2))
