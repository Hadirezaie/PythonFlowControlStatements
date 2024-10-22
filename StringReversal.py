from VowelCounter import result

s= input("Enter a string to reverse: ")
print(s[::-1])

#  another method
str = input("Enter a string to reverse: ")
i = len(str)-1
result = ''
while i>=0:
    result += str[i]
    i-=1
    print(result)