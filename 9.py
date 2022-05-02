# Problem 9 : Python Program to Calculate the Number of Words and 
# the Number of Characters Present in a String

str = input("Enter a string:")
count = 0
for x in str:
    if (x not in " "):
        count+=1

wordcount = 0
for i in range(len(str)):
    if (str[i]== " " and str[i+1]):
        wordcount += 1
wordcount += 1
print("Number of words:",wordcount)
print("Number of characters:",count)

