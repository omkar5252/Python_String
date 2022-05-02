# Problem 5 : Python Program to Count the Number of Vowels in a String

data = input("Enter a string:")
count = 0
for x in data:
    if (x in "aeiou"):
        count += 1
print("Number of vowels:",count)