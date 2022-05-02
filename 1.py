# Problen 1 : Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = input("Enter a string:")
print("Original string:",str)

str2 = " "
for i in range(0,len(str)):
    if (str[i] == "a"):
        str2 += "$"
    else:
        str2 += str[i]
print("Updated string:",str2)