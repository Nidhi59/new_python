# ques 8: python program to print an inverted star pattern

n = int(input("Enter the number of rows:"))
for i in range(n, 0, -1):
    print((n-i) * ' ' + i * '*')
