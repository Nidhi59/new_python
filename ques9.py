# ques 9 Python program to print table of a given number

n = int(input("Enter the number whose table is to be printed:"))
for i in range(1, 11):
    num = n*i
    print(n, "*", i, "=", num)
