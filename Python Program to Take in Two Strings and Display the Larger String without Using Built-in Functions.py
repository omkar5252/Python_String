# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = input("Enter a first string:")
str2 = input("Enter a second string:")

count1 = 0
for x in str1:
    count1+=1

count2 = 0
for x in str2:
    count2+=1

if (count1 < count2):
    print("Larger string is:",str2)
else:
    print("Larger string is:",str1)

