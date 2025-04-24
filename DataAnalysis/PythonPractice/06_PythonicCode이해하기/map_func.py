# 두 리스트 [1, 2, 3]과 [4, 5, 6]의 각 요소를 더한 새 리스트를 생성하세요. (map 함수 사용)

list1=[1,2,3]
list2=[4,5,6]
new_list = []
for i in list1,list2:
    new_list=list(map(lambda x,y : x+y , list1,list2))
    
print(new_list)