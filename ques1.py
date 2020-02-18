# ques 1 :  Python program to find largest number in the list

list1 = []
n = int(input("Enter the number of elements"))
for i in range(0, n):
    a = int(input("Enter the element:"))
    list1.append(a)

list1.sort()
print("Largest element is:", list1[n-1])
