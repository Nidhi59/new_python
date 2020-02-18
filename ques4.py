# ques 4:Python program  to merge two lists and sort them.

list1 = []
list2 = []
list3 = []

n = int(input("Enter the number of elements in list1"))
m = int(input("Enter the number of elements in list2"))

for i in range(0, n):
    a = int(input("Enter the element of first list:"))
    list1.append(a)


for i in range(0, m):
    b = int(input("Enter the element of second list:"))
    list2.append(b)

print("Elements of first list:", list1)
print("Elements of second list:", list2)

list3 = list1 + list2
print("Merged array is :", list3)

list3.sort()
print("sorted array is:", list3)
