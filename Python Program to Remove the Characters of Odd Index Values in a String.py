# Python Program to Remove the Characters of Odd Index Values in a String

str = input("Enter a string:")
print("Original string:",str)

str2 =" "
for i in range(len(str)):
    if (i % 2 == 0):
        str2 = str2 + str[i]
print("Modified string:",str2)
    
