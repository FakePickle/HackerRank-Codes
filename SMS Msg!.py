s = input()
vowel = ['a','e','i','o','u','A','E','I','O','U']
result = ''
for i in range(len(s)):
    if s[i] not in vowel:
        result += s[i]
print(result)