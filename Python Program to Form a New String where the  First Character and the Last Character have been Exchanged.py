# Python Program to Form a New String where the 
# First Character and the Last Character have been Exchanged

str = "firstbit"
n = len(str)

start = str[0]
end = str[n-1]

for i in range(0,len(str)):
    str2 = end + str[1:-1]+ start
print(str2)


