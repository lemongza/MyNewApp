#1부터 100까지의 숫자 중 3의 배수의 합을 구하세요.

sum=0
for i in range(1,101):
    if i%3==0 :
        sum+=i
print("3의 배수의 합:",sum)