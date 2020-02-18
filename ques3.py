# ques3: Python program to put even and odd numbers of a list into two seperate lists.

list1 = []
list2 = []
list3 = []

n = int(input("Enter the number of elements in the list"))
for i in range(0, n):
    a = int(input("Enter the element"))
    list1.append(a)
print(list1)

for x in list1:
    if x % 2 == 0:
        list2.append(x)

    else:
        list3.append(x)

print("All even elements are:", list2)
print("All odd elements are:", list3)
