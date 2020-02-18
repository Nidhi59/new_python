#  ques 2: Python program to find second largest number in the list

list1 = []
n = int(input("Enter the number of elements"))
for i in range(0, n):
    a = int(input("Enter the element:"))
    list1.append(a)

list1.sort()
print(" Second largest element is:", list1[n-2])
