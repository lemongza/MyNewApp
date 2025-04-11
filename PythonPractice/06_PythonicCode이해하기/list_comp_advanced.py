#[1, 2, 3, 4, 5]의 각 요소에 10을 더한 후 2로 나눈 결과를 리스트로 생성하세요. (리스트 컴프리헨션 사용)

list = [1,2,3,4,5]
new_list = [(x+10)/2 for x in list]

print (new_list)