# Problem 6 : Python Program to Take in a String and Replace Every Blank Space with Hyphen

str = input("Enter a string:")
print("Original string:",str)

str2 = " "
for x in str:
    if (x in " "):
        str2 += "-"
    else:
        str2 += x
print("Modified string:",str2)