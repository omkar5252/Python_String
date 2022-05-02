# Python Program to Detect if Two Strings are Anagrams

str1=input("Enter first string:")
str2 = input("Enter second string:")

str1 = list(str1)
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if (str1[i]) > (str1[j]):
            str1[i],str1[j] = str1[j],str1[i]

str2 = list(str2)
for i in range(len(str2)):
    for j in range(i+1,len(str2)):
        if (str2[i]) > (str2[j]):
            str2[i],str2[j] = str2[j],str2[i]

if (str1 == str2):
    print("Two strings are anagrams.")
else:
    print("Two strings are not anagrams.")


            


