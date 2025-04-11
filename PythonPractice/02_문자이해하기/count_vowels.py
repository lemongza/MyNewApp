#"Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.

str ="Python is awesome"
cnt = sum(str.count(vowel) for vowel in "aeiou")
print('모음 개수 :', cnt)

