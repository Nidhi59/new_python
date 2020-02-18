# ques 10 :Python program to find whether a number is a power of two.


def is_power_of_two(n):
    """  Return True if n is a power of two """

    if n <= 0:
        return False
    else:
        return n & (n-1) == 0


n = int(input("Enter the number :"))

if is_power_of_two(n):
    print(" {} number is a power of two " . format(n))

else:
    print("{} number is not the power of two" . format(n))
