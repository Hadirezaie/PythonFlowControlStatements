word= input("Enter a word: ")
vowels={'a','A','e','E','i','I','o','O','u','U'}
result={}
for letter in word:
    if letter in vowels:
        result[letter]=result.get(letter,0)+1
for l,n in sorted(result.items()):
    print(l,'is present ',n,'time(s)')