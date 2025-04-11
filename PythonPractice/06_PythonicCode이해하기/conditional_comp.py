#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수는 제곱, 홀수는 그대로인 새 리스트를 생성하세요. (조건부 리스트 컴프리헨션 사용)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for i in list :
    if i%2!=0:
        new_list.append(i)
    else :
        new_list.append(i**2)
        
print(new_list)