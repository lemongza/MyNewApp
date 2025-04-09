#10000원을 3명이서 똑같이 나누어 가질 때 각자 얼마를 받고 얼마가 남는지 계산하세요.

rest=10000
while rest>3 :
    money=int(rest/3)
    rest=rest%3


print(f"각자 {money}원을 받고 {rest}원이 남습니다.")