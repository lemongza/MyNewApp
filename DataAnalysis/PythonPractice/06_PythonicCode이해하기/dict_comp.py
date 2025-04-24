# ["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요. (딕셔너리 컴프리헨션 사용)

list = ["apple", "banana", "cherry"]
dict = {}

for i in list : 
    dict[i] = len(i)
    
print(dict)
