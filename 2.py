# Problem 2 : Python Program to Remove the nth Index Character from a Non-Empty String

str = input("Enter a string:")
n = int(input("Enter value nth index tobe removed:"))
str2 = " "
for i in range(0,len(str)):
    if (i != n):
        str2 += str[i]
print(str2)